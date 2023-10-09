import csv
from zipfile import ZipFile
from season_class_legacy import Season
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/seasons/legacy/dump/season_data_dump.csv', 'w+',  encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    column_headers = [
        'id',
        'team_id',
        'name',
        'start_date',
        'end_date',
        'link_allowed',
        'payment_schedule_state',
        'budget_shared',
        'discount_amount',
        'discount_cutoff_amount',
        'discount_cutoff_date',
        'discount_enabled',
        'created_at',
        'updated_at',
    ]
    outcsv.writerow(column_headers)
    id_lookup = {}

    with open('new_spend_tables/seasons/legacy/dump/season_bad_data.csv', 'w+', encoding='UTF-8', newline='') as bad_data_file:
        bad_data_file_csv = csv.writer(bad_data_file, delimiter=',')
        bad_data_file_csv.writerow(column_headers)

        with Session(engine) as session:
            records = session.query(Season).all()
            for col in records:
                id = 'spdsea_%s' % cuid()
                id_lookup[col.id] = id
                row = [
                    id,
                    col.team_id,
                    col.name,
                    col.start_date,
                    col.end_date,
                    col.link_allowed,
                    col.payment_schedule_state,
                    col.budget_shared,
                    col.discount_amount,
                    col.discount_cutoff_amount,
                    col.discount_cutoff_date,
                    col.discount_enabled,
                    col.created_at,
                    col.updated_at,
                ]
                if not col.team_id:
                    bad_data_file_csv.writerow(row)
                    # to skip writing rows that are bad data in the actual dump uncomment the line below
                    # continue
                outcsv.writerow(row)
            with open('new_spend_tables/seasons/idlookup/seasons_id_lookup.json', 'w+') as id_lookup_file:
                json.dump(id_lookup, id_lookup_file)
        bad_data_file.close()
    outfile.close()

with ZipFile('new_spend_tables/seasons/zipped/season_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/seasons/legacy/dump/season_data_dump.csv')
    zipObj.write(
        'new_spend_tables/seasons/idlookup/seasons_id_lookup.json')
    zipObj.close()

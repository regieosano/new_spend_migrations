import csv
from zipfile import ZipFile
from budget_class_legacy import Budget
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    column_headers = [
        'id',
        'description',
        'target_date',
        'target_amount',
        'payment_method_id',
        'season_id',
        'category_id',
        'created_at',
        'updated_at',
    ]
    outcsv.writerow(column_headers)
    id_lookup = {}

    with open('new_spend_tables/budget_items/legacy/dump/budget_bad_data.csv', 'w+', encoding='UTF-8', newline='') as bad_data_file:
        bad_data_file_csv = csv.writer(bad_data_file, delimiter=',')
        bad_data_file_csv.writerow(column_headers)

        with Session(engine) as session:
            records = session.query(Budget).all()
            for col in records:
                id = 'spdbud_%s' % cuid()
                id_lookup[col.id] = id
                row = [
                    id,
                    col.description,
                    col.target_date,
                    col.target_amount,
                    col.payment_method_id,
                    col.season_id,
                    col.category_id,
                    col.created_at,
                    col.updated_at,
                ]
                if not col.season_id or not col.category_id:
                    bad_data_file_csv.writerow(row)
                    # to skip writing rows that are bad data in the actual dump uncomment the line below
                    # continue
                outcsv.writerow(row)
            with open('new_spend_tables/budget_items/idlookup/budget_items_id_lookup.json', 'w+') as id_lookup_file:
                json.dump(id_lookup, id_lookup_file)
        bad_data_file.close()
    outfile.close()

with ZipFile('new_spend_tables/budget_items/zipped/budget_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv')
    zipObj.write(
        'new_spend_tables/budget_items/idlookup/budget_items_id_lookup.json')
    zipObj.close()

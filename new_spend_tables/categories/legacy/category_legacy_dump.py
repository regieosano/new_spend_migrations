import csv
from zipfile import ZipFile
from category_class_legacy import Category
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine as spend_dev_engine
from cuid import cuid
import json

session_pool = sessionmaker(spend_dev_engine)

with open('new_spend_tables/categories/legacy/dump/category_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    column_headers = [
        'id',
        'name',
        'org_id',
        'hidden',
        'created_at',
        'updated_at',
    ]
    outcsv.writerow(column_headers)
    id_lookup = {}

    with open('new_spend_tables/categories/legacy/dump/category_bad_data.csv', 'w+', encoding='UTF-8', newline='') as bad_data_file:
        bad_data_file_csv = csv.writer(bad_data_file, delimiter=',')
        bad_data_file_csv.writerow(column_headers)

        with Session(spend_dev_engine) as session:
            records = session.query(Category).all()
            for col in records:
                id = 'spdcat_%s' % cuid()
                id_lookup[col.id] = id
                row = [
                    id,
                    col.name,
                    col.org_id,
                    col.hidden,
                    col.created_at,
                    col.updated_at,
                ]
                if not col.org_id:
                    bad_data_file_csv.writerow(row)
                    # to skip writing rows that are bad data in the actual dump uncomment the line below
                    # continue
                outcsv.writerow(row)
            with open('new_spend_tables/categories/idlookup/categories_id_lookup.json', 'w+') as id_lookup_file:
                json.dump(id_lookup, id_lookup_file)
        bad_data_file.close()
    outfile.close()

with ZipFile('new_spend_tables/categories/zipped/category_data_dump.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/categories/legacy/dump/category_data_dump.csv')
    zipObj.write(
        'new_spend_tables/categories/idlookup/categories_id_lookup.json')
    zipObj.close()

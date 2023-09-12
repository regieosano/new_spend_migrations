import csv
from zipfile import ZipFile
from category_class_legacy import Category
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/categories/legacy/dump/category_data_dump.csv', 'w+', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'name',
        'type',
        'is_default',
        'is_hidden',
        'created_at',
        'updated_at',
        'organization_id',
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Category).all()
        for col in records:
            id = 'spdcat_%s' % cuid()
            id_lookup[col.id] = id
            if col.updated_at is None:
                updated_at = '2021-10-14 15:42:00.079246'
            else:
                updated_at = col.updated_at
            outcsv.writerow([
                id,
                col.name,
                None,
                False,
                col.hidden,
                col.created_at,
                updated_at,
                'spdorg_cliayn82a00bb6ot9786n562a',
            ])
        with open('new_spend_tables/categories/idlookup/categories_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

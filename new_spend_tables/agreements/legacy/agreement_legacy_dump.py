import csv
from agreement_class_legacy import Agreement
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine as spend_dev_engine
from cuid import cuid
import json

session_pool = sessionmaker(spend_dev_engine)

with open('new_spend_tables/agreements/legacy/dump/agreement_data_dump.csv', 'w+', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'org_id',
        'name',
        'content',
        'status',
        'created_at',
        'updated_at',
    ])
    id_lookup = {}
    with Session(spend_dev_engine) as session:
        records = session.query(Agreement).all()
        for col in records:
            id = 'spdagr_%s' % cuid()
            id_lookup[col.id] = id
            if col.updated_at is None:
                updated_at = '2023-01-01 00:00:00.000000'
            else:
                updated_at = col.updated_at
            outcsv.writerow([
                id,
                col.org_id,
                None,
                False,
                col.hidden,
                col.created_at,
                updated_at,

            ])
        with open('new_spend_tables/agreements/idlookup/agreements_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

import csv
from zipfile import ZipFile
from invite_class_legacy import Invite
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine as spend_dev_engine
from cuid import cuid
import json

session_pool = sessionmaker(spend_dev_engine)

with open('new_spend_tables/invites/legacy/dump/invite_data_dump.csv', 'w+', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'email',
        'token',
        'message_id',
        'type',
        'status',
        'created_at',
        'updated_at',
    ])
    id_lookup = {}
    with Session(spend_dev_engine) as session:
        records = session.query(Invite).all()
        for col in records:
            id = 'spdinv_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.email,
                col.token,
                col.message_id,
                col.type,
                col.status,
                col.created_at,
                col.updated_at,

            ])
        with open('new_spend_tables/invites/idlookup/invites_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/invites/zipped/invite_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/invites/legacy/dump/invite_data_dump.csv')
    zipObj.write(
        'new_spend_tables/invites/idlookup/invites_id_lookup.json')
    zipObj.close()

import csv
from zipfile import ZipFile
from notifications_class_legacy import Notifications
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/notifications/legacy/dump/notifications_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'past_due',
        'failed_payment',
        'created_at',
        'updated_at',
        'org_level',
        'club_user_level',
        'team_user_level',
        'snap_home_notify',
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Notifications).all()
        for col in records:
            id = 'spdnot_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.past_due,
                col.failed_payment,
                col.created_at,
                col.updated_at,
                col.org_level,
                col.club_user_level  ,
                col.team_user_level,
                col.snap_home_notify,
            ])
        with open('new_spend_tables/notifications/idlookup/notifications_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close() 

with ZipFile('new_spend_tables/notifications/zipped/notifications_csv_json.zip', 'w') as zipObj:
    zipObj.write('new_spend_tables/notifications/legacy/dump/notifications_data_dump.csv')
    zipObj.write('new_spend_tables/notifications/idlookup/notifications_id_lookup.json')
    zipObj.close()          
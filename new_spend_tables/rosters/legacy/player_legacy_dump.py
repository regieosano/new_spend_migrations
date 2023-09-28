import csv
from zipfile import ZipFile
from player_class_legacy import Player
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/rosters/legacy/dump/player_data_dump.csv', 'w+',  encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'player_id',
        'player_name',
        'dob',
        'archived',

    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Player).all()
        for col in records:
            id = 'spdply_%s' % cuid()
            id_lookup[col.player_id] = id

            outcsv.writerow([
                id,
                col.player_name,
                col.dob,
                col.archived,

            ])
        with open('new_spend_tables/rosters/idlookup/rosters_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/rosters/zipped/player_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/rosters/legacy/dump/player_data_dump.csv')
    zipObj.write(
        'new_spend_tables/rosters/idlookup/rosters_id_lookup.json')
    zipObj.close()

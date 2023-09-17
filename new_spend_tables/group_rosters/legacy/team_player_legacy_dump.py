import csv
from zipfile import ZipFile
from team_player_class_legacy import Team_Player
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'team_id',
        'player_id',
        'payer_id',
        'join_date',
        'add_date',
        'archived',
        'invite_id',
        'payer_initiated',
        'agreement_id',
        'season_id',
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Team_Player).all()
        for col in records:
            id = 'spdtp_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.team_id,
                col.player_id,
                col.payer_id,
                col.join_date,
                col.add_date,
                col.archived,
                col.invite_id,
                col.payer_initiated,
                col.agreement_id,
                col.season_id,
            ])
        with open('new_spend_tables/group_rosters/idlookup/team_player_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/group_rosters/zipped/team_player_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv')
    zipObj.write(
        'new_spend_tables/group_rosters/idlookup/team_player_id_lookup.json')
    zipObj.close()

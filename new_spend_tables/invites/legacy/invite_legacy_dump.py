import csv
from zipfile import ZipFile
from invite_class_legacy import Invite
from new_spend_tables.team_player.legacy.team_player_legacy import TeamPlayer
from new_spend_tables.groups.legacy.team_class_legacy import Team
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
        'org_id',
    ])
    id_lookup = {}
    with Session(spend_dev_engine) as session:
        records = session.query(Invite).all()
        for col in records:
            org_id = ''
            team_player = session.query(TeamPlayer).filter_by(invite_id=col.id).first()
            if team_player:
                team = session.query(Team).filter_by(team_id=team_player.team_id).first()
                if team.org_id:
                    org_id = team.org_id
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
                org_id,
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

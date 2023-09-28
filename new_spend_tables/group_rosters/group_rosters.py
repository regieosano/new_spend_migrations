import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from group_rosters_class import Group_Rosters
from _database.engine_db import engine

source_csv_file = "new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv"

session_pool = sessionmaker(engine)

team_player_data = pd.read_csv(source_csv_file)

DUMMY_VALID_DATE = '2023-01-01 00:00:00.000000'

# Initialize look-up tables
group_id_lookup_file = open(
    'new_spend_tables/groups/idlookup/groups_id_lookup.json')
group_id_lookup = json.load(group_id_lookup_file)

invite_id_lookup_file = open(
    'new_spend_tables/invites/idlookup/invites_id_lookup.json')
invite_id_lookup = json.load(invite_id_lookup_file)

record = team_player_data.to_dict()

for i in range(len(team_player_data)):
    # Get values of new PK from lookup tables based on mapping from legacy
    group_id_value = group_id_lookup[str(record['team_id'][i])]
    invite_id_value = invite_id_lookup[str(int(record['invite_id'][i]))]
    archived_value = True if record['archived'][i] == 'True' else False
    group_roster = Group_Rosters(
        id=record['id'][i],
        roster_id=record['team_id'][i],
        user_id=record['player_id'][i],
        group_id=group_id_value,
        invite_id=invite_id_value,
        season_id=record['season_id'][i],
        is_archived=archived_value,
        archived_at=DUMMY_VALID_DATE,
        joined_at=record['join_date'][i],
        is_member_initiated=False,
        created_at=DUMMY_VALID_DATE,
    )

    with Session(engine) as session:
        session.add(group_roster)
        session.commit()

# with open(source_csv_file, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # Get values of new PK from lookup tables based on mapping from legacy
#         group_id_value = group_id_lookup[row['team_id']]
#         invite_id_value = invite_id_lookup[row['invite_id']]

#         archived_value = True if row['archived'] == 'True' else False
#         created_at_value = '2023-01-01 00:00:00.000000'

#         group_roster = Group_Rosters(
#             id=row['id'],
#             roster_id=row['team_id'],
#             user_id=row['player_id'],
#             group_id=group_id_value,
#             invite_id=invite_id_value,
#             season_id=row['season_id'],
#             is_archived=archived_value,
#             archived_at='2023-01-01 00:00:00.000000',
#             joined_at=row['join_date'],
#             is_member_initiated=False,
#             created_at=created_at_value,
#         )

#         with Session(engine) as session:
#             session.add(group_roster)
#             session.commit()

import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from group_rosters_class import Group_Rosters
from _database.engine_db import engine

source_csv_file = "new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv"

session_pool = sessionmaker(engine)

team_player_data = pd.read_csv(source_csv_file)

DUMMY_VALID_INVT_ID = 'TEMP - INVT-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_USR_ID = 'TEMP - USER-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_ROSTR_ID = 'TEMP - ROSTR-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_DATE = '2023-01-01 00:00:00.000000'

# Initialize look-up tables
group_id_lookup_file = open(
    'new_spend_tables/groups/idlookup/groups_id_lookup.json')
group_id_lookup = json.load(group_id_lookup_file)

invite_id_lookup_file = open(
    'new_spend_tables/invites/idlookup/invites_id_lookup.json')
invite_id_lookup = json.load(invite_id_lookup_file)
rosters_id_lookup_file = open(
    'new_spend_tables/rosters/idlookup/rosters_id_lookup.json')
rosters_id_lookup = json.load(rosters_id_lookup_file)
seasons_id_lookup_file = open(
    'new_spend_tables/seasons/idlookup/seasons_id_lookup.json')
seasons_id_lookup = json.load(seasons_id_lookup_file)

record = team_player_data.to_dict()

for i in range(len(team_player_data)):
    # Get values of new PK from lookup tables based on mapping from legacy
    group_id_value = group_id_lookup[str(record['team_id'][i])]
    invite_id_value = DUMMY_VALID_INVT_ID if pd.isna(
        record['invite_id'][i]) else invite_id_lookup[str(int(record['invite_id'][i]))]
    rosters_id_value = DUMMY_VALID_ROSTR_ID if pd.isna(
        record['player_id'][i]) else rosters_id_lookup[record['player_id'][i]]
    seasons_id_value = seasons_id_lookup[str(record['season_id'][i])]
    archived_value = True if record['archived'][i] == 'True' else False
    joined_at_value = DUMMY_VALID_DATE if pd.isna(
        record['join_date'][i]) else record['join_date'][i]

    group_roster = Group_Rosters(
        id=record['id'][i],
        roster_id=rosters_id_value,
        user_id=DUMMY_VALID_USR_ID,
        group_id=group_id_value,
        invite_id=invite_id_value,
        season_id=seasons_id_value,
        is_archived=archived_value,
        archived_at=DUMMY_VALID_DATE,
        joined_at=joined_at_value,
        is_member_initiated=False,
        created_at=DUMMY_VALID_DATE,
    )

    with Session(engine) as session:
        session.add(group_roster)
        session.commit()

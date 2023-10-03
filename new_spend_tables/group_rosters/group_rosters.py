import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from group_rosters_class import Group_Rosters
from _database.engine_db import engine

source_csv_file = "new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv"

session_pool = sessionmaker(engine)

team_player_data = pd.read_csv(source_csv_file)

DUMMY_VALID_SEASON_ID = 'TEMP - SEAS-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_ROSTER_ID = 'TEMP - ROSTR-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_INVITE_ID = 'TEMP - INVT-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_GROUP_ID = 'TEMP - GRP-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_DATE = '2023-01-01 00:00:00.000000'


# Initialize look-up tables
group_id_lookup_file = open(
    'new_spend_tables/groups/idlookup/groups_id_lookup.json')
group_id_lookup = json.load(group_id_lookup_file)

invite_id_lookup_file = open(
    'new_spend_tables/invites/idlookup/invites_id_lookup.json')
invite_id_lookup = json.load(invite_id_lookup_file)

roster_id_lookup_file = open(
    'new_spend_tables/rosters/idlookup/rosters_id_lookup.json')
roster_id_lookup = json.load(roster_id_lookup_file)
season_id_lookup_file = open(
    'new_spend_tables/seasons/idlookup/seasons_id_lookup.json')
season_id_lookup = json.load(season_id_lookup_file)


record = team_player_data.to_dict()

for i in range(len(team_player_data)):
    # Get values of new PK from lookup tables based on mapping from legacy
    group_id_value = DUMMY_VALID_GROUP_ID if pd.isna(record['team_id'][i]) else group_id_lookup[record['team_id'][i]]
    invite_id_value = DUMMY_VALID_INVITE_ID if pd.isna(record['invite_id'][i]) else invite_id_lookup[str(int(record['invite_id'][i]))]
    roster_id_value = DUMMY_VALID_ROSTER_ID if pd.isna(record['player_id'][i]) else roster_id_lookup[record['player_id'][i]]
    season_id_value = DUMMY_VALID_SEASON_ID if pd.isna(str(record['season_id'][i])) else season_id_lookup[str(record['season_id'][i])]
    archived_value = True if record['archived'][i] == 'True' else False
    member_initiated_value = True if record['payer_initiated'][i] == 'True' else False
    joined_at_value = DUMMY_VALID_DATE if pd.isna(
        record['join_date'][i]) else record['join_date'][i]
    created_at_value = DUMMY_VALID_DATE if pd.isna(
        record['add_date'][i]) else record['add_date'][i]
    group_roster = Group_Rosters(
        id=record['id'][i],
        roster_id=roster_id_value,
        user_id='TEMP - USER-00000000-0000-0000-0000-000000000000',
        group_id=group_id_value,
        invite_id=invite_id_value,
        season_id=season_id_value,
        is_archived=archived_value,
        archived_at=DUMMY_VALID_DATE,
        joined_at=joined_at_value,
        is_member_initiated=member_initiated_value,
        created_at=created_at_value,
    )

    with Session(engine) as session:
        session.add(group_roster)
        session.commit()


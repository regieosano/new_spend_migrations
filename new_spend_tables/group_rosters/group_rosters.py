import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from group_rosters_class import Group_Rosters
from _lookup.lookup_tables import group_id_lookup, invite_id_lookup, roster_id_lookup, season_id_lookup
from _dummy.dummy_data_values import DUMMY_VALID_GROUP_ID, DUMMY_VALID_INVITE_ID, DUMMY_VALID_ROSTER_ID, DUMMY_VALID_SEASON_ID, DUMMY_VALID_DATE
from _database.engine_db import engine

source_csv_file = "new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv"

session_pool = sessionmaker(engine)

team_player_data = pd.read_csv(source_csv_file)

LENGTH_OF_TEAM_PLAYER_DATA = len(team_player_data)

record = team_player_data.to_dict()

for i in range(LENGTH_OF_TEAM_PLAYER_DATA):
    # Get values of new PK from lookup tables based on mappings from legacy
    try:
        group_id_value = DUMMY_VALID_GROUP_ID if pd.isna(record['team_id'][i]) else group_id_lookup[record['team_id'][i]]
    except KeyError:
        group_id_value = DUMMY_VALID_GROUP_ID

    try:
        invite_id_value = DUMMY_VALID_INVITE_ID if pd.isna(record['invite_id'][i]) else invite_id_lookup[str(int(record['invite_id'][i]))]
    except KeyError:
        invite_id_value = DUMMY_VALID_INVITE_ID

    try:
        roster_id_value = DUMMY_VALID_ROSTER_ID if pd.isna(record['player_id'][i]) else roster_id_lookup[record['player_id'][i]]
    except KeyError:
        roster_id_value = DUMMY_VALID_ROSTER_ID

    try:
        season_id_value = DUMMY_VALID_SEASON_ID if pd.isna(str(record['season_id'][i])) else season_id_lookup[str(record['season_id'][i])]
    except KeyError:
        season_id_value = DUMMY_VALID_SEASON_ID

    try:
        archived_value = True if record['archived'][i] == 'True' else False
    except:
        archived_value = False

    try:
        member_initiated_value = True if record['payer_initiated'][i] == 'True' else False
    except:
        member_initiated_value = False

    try:
        joined_at_value = DUMMY_VALID_DATE if pd.isna(record['join_date'][i]) else record['join_date'][i]
    except:
        joined_at_value = DUMMY_VALID_DATE

    try:
        created_at_value = DUMMY_VALID_DATE if pd.isna(record['add_date'][i]) else record['add_date'][i]
    except:
        created_at_value = DUMMY_VALID_DATE
        
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


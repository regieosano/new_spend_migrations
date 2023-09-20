import csv
import uuid

from sqlalchemy.orm import Session, sessionmaker
from group_rosters_class import Group_Rosters
from _database.engine_db import engine

source_csv_file = "new_spend_tables/group_rosters/legacy/dump/team_player_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        archived_value = True if row['archived'] == 'True' else False
        created_at_value = '2023-01-01 00:00:00.000000' if row['created_at'] == '' else row['created_at']
        organization_id_value = 'spdorg_clmgc6vab00002v15vr2l22jy' if row[
            'org_id'] == '' else row['org_id']
        group_roster = Group_Rosters(
            id=row['id'],
            roster_id=row['team_id'],
            user_id=row['player_id'],
            group_id=row['payer_id'],
            invite_id=row['invite_id'],
            season_id=row['season_id'],
            is_archived=archived_value,
            archived_at='2023-01-01 00:00:00.000000',
            joined_at=row['join_date'],
            is_member_initiated=False,
            created_at=created_at_value,
        )

        with Session(engine) as session:
            session.add(group_roster)
            session.commit()

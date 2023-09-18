import csv
from cuid import cuid
from sqlalchemy.orm import Session, sessionmaker
from invites_class import Invites
from _database.engine_db import engine as new_spend_db_engine

source_csv_file = "new_spend_tables/invites/legacy/dump/invite_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        invite = Invites(
            id=row['id'],
            first_name='',
            last_name='',
            email=row['email'],
            type=row['type'],
            is_user=False,
            status=row['status'],
            organization_id='',
            group_id='',
            user_id='',
            is_archived=False,
            created_at=row['created_at'],
            expires_at='2023-01-01 00:00:00.000000'
        )

        with Session(new_spend_db_engine) as session:
            session.add(invite)
            session.commit()

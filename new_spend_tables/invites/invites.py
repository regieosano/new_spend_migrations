import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from invites_class import Invites
from _database.engine_db import engine as new_spend_db_engine

source_csv_file = "new_spend_tables/invites/legacy/dump/invite_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

data = pd.read_csv(source_csv_file)

LENGTH_OF_DATA = len(data) - 1

for i in range(LENGTH_OF_DATA):
    record = data.to_dict()
    invite = Invites(
        id=record['id'][i],
        first_name='',
        last_name='',
        email=record['email'][i],
        type=record['type'][i],
        is_user=False,
        status=record['status'][i],
        organization_id='',
        group_id='',
        user_id='',
        is_archived=False,
        created_at=record['created_at'][i],
        expires_at='2023-01-01 00:00:00.000000'
    )

    with Session(new_spend_db_engine) as session:
        session.add(invite)
        session.commit()

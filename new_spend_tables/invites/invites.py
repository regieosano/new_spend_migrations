import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from invites_class import Invites
from _database.engine_db import engine as new_spend_db_engine

source_csv_file = "new_spend_tables/invites/legacy/dump/invite_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

invite_data = pd.read_csv(source_csv_file)

DUMMY_VALID_ORG_ID = 'TEMP - ORG-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_GRP_ID = 'TEMP - GRP-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_USR_ID = 'TEMP - USER-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_DATE = '2023-01-01 00:00:00.000000'

LENGTH_OF_INVITE_DATA = len(invite_data) - 1

record = invite_data.to_dict()

for i in range(LENGTH_OF_INVITE_DATA):
    invite = Invites(
        id=record['id'][i],
        first_name='',
        last_name='',
        email=record['email'][i],
        type=record['type'][i],
        is_user=False,
        status=record['status'][i],
        organization_id=DUMMY_VALID_ORG_ID,
        group_id=DUMMY_VALID_GRP_ID,
        user_id=DUMMY_VALID_USR_ID,
        is_archived=False,
        created_at=record['created_at'][i],
        expires_at=DUMMY_VALID_DATE
    )

    with Session(new_spend_db_engine) as session:
        session.add(invite)
        session.commit()

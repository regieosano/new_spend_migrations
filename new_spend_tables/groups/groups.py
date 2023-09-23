import csv
import uuid

from sqlalchemy.orm import Session, sessionmaker
from groups_class import Groups
from _database.engine_db import engine

source_csv_file = "new_spend_tables/groups/legacy/dump/group_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        archived_value = True if row['archived'] == 'True' else False
        created_at_value = '2023-01-01 00:00:00.000000' if row['created_at'] == '' else row['created_at']
        organization_id_value = 'spdorg_clmgc6vab00002v15vr2l22jy' if row[
            'org_id'] == '' else row['org_id']
        group = Groups(
            id=row['team_id'],
            name=row['team_name'],
            vault_id=uuid.uuid4(),
            prog_id=uuid.uuid4(),
            is_archived=archived_value,
            created_at=created_at_value,
            archived_at='2023-01-01 00:00:00.000000',
            organization_id='spdorg_clmsygor50000j8ny54q0b140',
            account_id=row['account_id'],
        )

        with Session(engine) as session:
            session.add(group)
            session.commit()

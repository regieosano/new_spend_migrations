import uuid
import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from groups_class import Groups
from _database.engine_db import engine

source_csv_file = "new_spend_tables/groups/legacy/dump/group_data_dump.csv"

session_pool = sessionmaker(engine)

group_data = pd.read_csv(source_csv_file)

LENGTH_OF_GROUP_DATA = len(group_data)

# Initialize look-up tables
organization_id_lookup_file = open(
    'new_spend_tables/organizations/idlookup/organization_id_lookup.json')
organization_id_lookup = json.load(organization_id_lookup_file)

record = group_data.to_dict()

for i in range(LENGTH_OF_GROUP_DATA):
    archived_value = True if record['archived'][i] == 'TRUE' else False
    created_at_value = '2023-01-01 00:00:00.000000' if record['created_at'][i] == '' else record['created_at'][i]
    organization_id_value = 'spdorg_clmgc6vab00002v15vr2l22jy' if record[
        'org_id'][i] == '' else organization_id_lookup[record['org_id'][i]]
    group = Groups(
        id=record['team_id'][i],
        name=record['team_name'][i],
        vault_id=uuid.uuid4(),
        prog_id=uuid.uuid4(),
        is_archived=archived_value,
        created_at=created_at_value,
        archived_at='2023-01-01 00:00:00.000000',
        organization_id=organization_id_value,
        account_id=record['account_id'][i],
    )

    with Session(engine) as session:
        session.add(group)
        session.commit()
# with open(source_csv_file, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         archived_value = True if row['archived'] == 'True' else False
#         created_at_value = '2023-01-01 00:00:00.000000' if row['created_at'] == '' else row['created_at']
#         organization_id_value = 'spdorg_clmgc6vab00002v15vr2l22jy' if row[
#             'org_id'] == '' else row['org_id']
#         group = Groups(
#             id=row['team_id'],
#             name=row['team_name'],
#             vault_id=uuid.uuid4(),
#             prog_id=uuid.uuid4(),
#             is_archived=archived_value,
#             created_at=created_at_value,
#             archived_at='2023-01-01 00:00:00.000000',
#             organization_id='spdorg_clmsygor50000j8ny54q0b140',
#             account_id=row['account_id'],
#         )

#         with Session(engine) as session:
#             session.add(group)
#             session.commit()

import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from groups_class import Groups
from _database.engine_db import engine
from _lookup.lookup_tables import organization_id_lookup
from cuid import cuid

source_csv_file = "new_spend_tables/groups/legacy/dump/group_data_dump.csv"

session_pool = sessionmaker(engine)

group_data = pd.read_csv(source_csv_file)

LENGTH_OF_GROUP_DATA = len(group_data)

record = group_data.to_dict()

for i in range(LENGTH_OF_GROUP_DATA):
    archived_value = True if record['archived'][i] == 'TRUE' else False
    created_at_value = None if record['created_at'][i] == '' else record['created_at'][i]
    organization_id_value = organization_id_lookup[str(record['org_id'][i])]
    group = Groups(
        id=record['team_id'][i],
        name=record['team_name'][i],
        prog_id=f'NULL {cuid()}',
        is_archived=archived_value,
        created_at=created_at_value,
        organization_id=organization_id_value,
        account_id=record['account_id'][i],
    )

    with Session(engine) as session:
        session.add(group)
        session.commit()

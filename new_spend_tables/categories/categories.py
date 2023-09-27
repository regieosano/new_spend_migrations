import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from categories_class import Categories
from _database.engine_db import engine

source_csv_file = "new_spend_tables/categories/legacy/dump/category_data_dump.csv"

session_pool = sessionmaker(engine)

category_data = pd.read_csv(source_csv_file)

LENGTH_OF_CATEGORY_DATA = len(category_data)

# Initialize look-up tables
organization_id_lookup_file = open(
    'new_spend_tables/organizations/idlookup/organization_id_lookup.json')
organization_id_lookup = json.load(organization_id_lookup_file)

record = category_data.to_dict()

for i in range(LENGTH_OF_CATEGORY_DATA):
    updated_at_value = None if pd.isna(
        record['updated_at'][i]) else record['updated_at'][i]

    category = Categories(
        id=record['id'][i],
        name=record['name'][i],
        type='',
        is_default=False,
        is_hidden=record['hidden'][i],
        created_at=record['created_at'][i],
        updated_at=updated_at_value,
        organization_id=organization_id_lookup[str(record['org_id'][i])]
    )

    with Session(engine) as session:
        session.add(category)
        session.commit()

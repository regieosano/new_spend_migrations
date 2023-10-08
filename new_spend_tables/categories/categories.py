import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from categories_class import Categories
from _lookup.lookup_tables import organization_id_lookup
from _dummy.dummy_data_values import DUMMY_VALID_ORGANIZATION_ID
from _database.engine_db import engine

source_csv_file = "new_spend_tables/categories/legacy/dump/category_data_dump.csv"

session_pool = sessionmaker(engine)

category_data = pd.read_csv(source_csv_file)

LENGTH_OF_CATEGORY_DATA = len(category_data)

record = category_data.to_dict()

for i in range(LENGTH_OF_CATEGORY_DATA):
    try:
        updated_at_value = None if pd.isna(record['updated_at'][i]) else record['updated_at'][i]
    except KeyError:
        updated_at_value = None

    try:
        organization_id_value = DUMMY_VALID_ORGANIZATION_ID if pd.isna(str(record['org_id'][i])) else organization_id_lookup[str(record['org_id'][i])]       
    except:
        organization_id_value = DUMMY_VALID_ORGANIZATION_ID   

    category = Categories(
        id=record['id'][i],
        name=record['name'][i],
        type='',
        is_default=False,
        is_hidden=record['hidden'][i],
        created_at=record['created_at'][i],
        updated_at=updated_at_value,
        organization_id=organization_id_value
    )

    with Session(engine) as session:
        session.add(category)
        session.commit()

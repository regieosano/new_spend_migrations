import json
import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from budget_items_class import Budget_Items
from _database.engine_db import engine as prod_engine

source_csv_file = "new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv"

session_pool = sessionmaker(prod_engine)

budget_data = pd.read_csv(source_csv_file)

DUMMY_VALID_SEASON_ID = 'SEAS-00000000-0000-0000-0000-000000000000'
DUMMY_VALID_DATE = '2023-01-01 00:00:00.000000'
LENGTH_OF_BUDGET_DATA = len(budget_data)

# Initialize look-up tables
season_id_lookup_file = open(
    'new_spend_tables/seasons/idlookup/seasons_id_lookup.json')
season_id_lookup = json.load(season_id_lookup_file)
category_id_lookup_file = open(
    'new_spend_tables/categories/idlookup/categories_id_lookup.json')
category_id_lookup = json.load(category_id_lookup_file)

record = budget_data.to_dict()

for i in range(LENGTH_OF_BUDGET_DATA):
    created_at_value = DUMMY_VALID_DATE if pd.isna(
        record['created_at'][i]) else record['created_at'][i]
    updated_at_value = DUMMY_VALID_DATE if pd.isna(
        record['updated_at'][i]) else record['updated_at'][i]
    if pd.isna(record['season_id'][i]):
        season_id_value = DUMMY_VALID_SEASON_ID
    else:
        season_id_value = season_id_lookup[str(int(record['season_id'][i]))]
    category_id_value = category_id_lookup[str(record['category_id'][i])]
    budget_item = Budget_Items(
        id=record['id'][i],
        target_amount=record['target_amount'][i],
        target_date_at=record['target_date'][i],
        vault_id='',
        is_default=False,
        created_at=created_at_value,
        updated_at=updated_at_value,
        season_id=season_id_value,
        category_id=category_id_value,
        description=record['description'][i],
    )

    with Session(prod_engine) as session:
        session.add(budget_item)
        session.commit()

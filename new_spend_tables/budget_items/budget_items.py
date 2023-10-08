import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from budget_items_class import Budget_Items
from _lookup.lookup_tables import season_id_lookup, category_id_lookup
from _database.engine_db import engine as prod_engine
from _dummy.dummy_data_values import DUMMY_VALID_CATEGORY_ID, DUMMY_VALID_SEASON_ID, DUMMY_VALID_DATE

source_csv_file = "new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv"

session_pool = sessionmaker(prod_engine)

budget_data = pd.read_csv(source_csv_file)

LENGTH_OF_BUDGET_DATA = len(budget_data)

record = budget_data.to_dict()

for i in range(LENGTH_OF_BUDGET_DATA):
    try:
        created_at_value = DUMMY_VALID_DATE if pd.isna(record['created_at'][i]) else record['created_at'][i]
    except:
        created_at_value = DUMMY_VALID_DATE

    try:
        updated_at_value = DUMMY_VALID_DATE if pd.isna(record['updated_at'][i]) else record['updated_at'][i]    
    except:
        updated_at_value = DUMMY_VALID_DATE

    try:
        season_id_value = DUMMY_VALID_SEASON_ID if pd.isna(record['season_id'][i]) else season_id_lookup[str(int(record['season_id'][i]))]    
    except:
        season_id_value = DUMMY_VALID_SEASON_ID

    try: 
        category_id_value = category_id_lookup[str(int(record['category_id'][i]))]    
    except:
        category_id_value = DUMMY_VALID_CATEGORY_ID
    
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

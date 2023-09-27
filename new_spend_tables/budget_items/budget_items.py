import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from budget_items_class import Budget_Items
from _database.engine_db import engine as prod_engine
import json


source_csv_file = "new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv"

session_pool = sessionmaker(prod_engine)

budget_data = pd.read_csv(source_csv_file)

LENGTH_OF_BUDGET_DATA = len(budget_data)

# Initialize look-up tables
season_id_lookup_file = open(
    'new_spend_tables/seasons/idlookup/seasons_id_lookup.json')
season_id_lookup = json.load(season_id_lookup_file)
category_id_lookup_file = open(
    'new_spend_tables/categories/idlookup/categories_id_lookup.json')
category_id_lookup = json.load(category_id_lookup_file)

record = budget_data.to_dict()


# with open(source_csv_file, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         created_at_value = '2023-01-01 00:00:00.000000' if row['created_at'] == '' else row['created_at']
#         updated_at_value = '2023-01-01 00:00:00.000000' if row['updated_at'] == '' else row['updated_at']
#         season_id_value = 'spdsea_clmuwp6j00ddx70ny19t2az13' if row[
#             'season_id'] == '' else season_id_lookup[row['season_id']]
#         category_id_value = category_id_lookup[row['category_id']]
#         budget_item = Budget_Items(
#             id=row['id'],
#             target_amount=row['target_amount'],
#             target_date_at='2023-01-01 00:00:00.000000',
#             vault_id='',
#             is_default=False,
#             created_at=created_at_value,
#             updated_at=updated_at_value,
#             season_id=season_id_value,
#             category_id=category_id_value,
#             description=row['description'],
#         )

#         with Session(prod_engine) as session:
#             session.add(budget_item)
#             session.commit()

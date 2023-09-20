import csv
from sqlalchemy.orm import Session, sessionmaker
from budget_items_class import Budget_Items
from _database.engine_db import engine as prod_engine
# from _prod_database.prod_engine_db import prod_engine


source_csv_file = "new_spend_tables/budget_items/legacy/dump/budget_items_data_dump.csv"


session_pool = sessionmaker(prod_engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # is_default_value = True if row['is_default'] == 'TRUE' else False
        created_at_value = '2023-01-01 00:00:00.000000' if row['created_at'] == '' else row['created_at']
        updated_at_value = '2023-01-01 00:00:00.000000' if row['updated_at'] == '' else row['updated_at']
        budget_item = Budget_Items(
            id=row['id'],
            target_amount=row['target_amount'],
            target_date_at='2023-01-01 00:00:00.000000',
            vault_id='-',
            is_default=False,
            created_at=created_at_value,
            updated_at=updated_at_value,
            season_id=row['season_id'],
            category_id=row['category_id'],
            description=row['description'],
        )

        with Session(prod_engine) as session:
            session.add(budget_item)
            session.commit()

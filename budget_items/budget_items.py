import csv
from sqlalchemy.orm import Session, sessionmaker
from budget_items_class import Budget_Items
from _database.engine_db import engine


source_file2 = "budget_items/budget_items_202308181605.csv"


session_pool = sessionmaker(engine)

with open(source_file2, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_default_value = True if row['is_default'] == 'TRUE' else False
        budget_item = Budget_Items(
            id=row['id'],
            target_amount=row['target_amount'],
            target_date_at=row['target_date_at'],
            vault_id=row['vault_id'],
            is_default=is_default_value,
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            season_id=row['season_id'],
            category_id=row['category_id'],
            description=row['description'],
        )

        with Session(engine) as session:
            session.add(budget_item)
            session.commit()

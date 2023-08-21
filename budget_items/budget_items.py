import csv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session, sessionmaker
from environs import Env
from budget_items_class import Budget_Items

env = Env()
env.read_env(".env")

source_file2 = "budget_items/budget_items_202308181605.csv"

url = URL.create(
    drivername=env.str("SERVER_DRIVERNAME"),
    username=env.str("H_IAM_USER"),
    password=env.str("H_IAM_PASSWORD"),
    host=env.str("H_PERSONAL_HOST"),
    port=env.int("H_PORT"),
    database=env.str("H_TEST_DATABASE"),
)

engine = create_engine(url, echo=True)
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

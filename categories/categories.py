import csv

from sqlalchemy.orm import Session, sessionmaker
from categories_class import Categories
from _database.engine_db import engine

source_csv_file = "categories/category_test_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_default_value = True if row['is_default'] == 'TRUE' else False
        is_hidden_value = True if row['is_hidden'] == 'TRUE' else False
        category = Categories(
            id=row['id'],
            name=row['name'],
            type=row['type'],
            is_default=is_default_value,
            is_hidden=is_hidden_value,
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            organization_id=row['organization_id'],
        )

        with Session(engine) as session:
            session.add(category)
            session.commit()

import csv

from sqlalchemy.orm import Session, sessionmaker
from categories_class import Categories
from _database.engine_db import engine

source_csv_file = "new_spend_tables/categories/legacy/dump/category_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_default_value = True if row['is_default'] == 'TRUE' else False
        is_hidden_value = True if row['is_hidden'] == 'TRUE' else False
        created_at_value = None if row['created_at'] == '' else row['created_at']
        updated_at_value = None if row['updated_at'] == '' else row['updated_at']
        organization_id_value = 'spdorg_clmsygor50000j8ny54q0b140' if row[
            'organization_id'] == '' else row['organization_id']
        category = Categories(
            id=row['id'],
            name=row['name'],
            type=row['type'],
            is_default=is_default_value,
            is_hidden=is_hidden_value,
            created_at=created_at_value,
            updated_at=updated_at_value,
            organization_id=organization_id_value
        )

        with Session(engine) as session:
            session.add(category)
            session.commit()

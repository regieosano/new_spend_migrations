import csv

from sqlalchemy.orm import Session, sessionmaker
from sales_class import Sales
from _database.engine_db import engine

source_csv_file = "new_spend_tables/sales/sales_test_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sale = Sales(
            id=row['id'],
            name=row['name'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
        )

        with Session(engine) as session:
            session.add(sale)
            session.commit()

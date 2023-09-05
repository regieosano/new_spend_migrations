import csv

from sqlalchemy.orm import Session, sessionmaker
from transactions_class import Transactions
from _database.engine_db import engine


source_csv_file = "transactions/transaction_test_data_dump.csv"


session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        transaction = Transactions(
            id=row['id'],
            source=row['source_id'],
            external_id=row['external_id'],
            invoice_id=row[''],
            is_reconciled=False,
        )

        with Session(engine) as session:
            session.add(transaction)
            session.commit()

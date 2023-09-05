import csv

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from transactions_class import Transactions
from legacy.transaction_class_legacy import Transaction
from legacy.invoice_transaction_class_legacy import Invoice_Transaction
from _database.engine_db import engine as new_spend_db_engine
from _database.engine_db_legacy import engine as legacy_engine


source_csv_file = "new_spend_tables/transactions/transaction_test_data_dump.csv"
legacy_session = Session(legacy_engine)


session_pool = sessionmaker(new_spend_db_engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Query a table to get the invoice_id
        stmt = select(Invoice_Transaction).where(
            Invoice_Transaction.id == Transaction.id)
        result = legacy_session.execute(stmt).fetchall()
        print(result)
        # transaction = Transactions(
        #     id=row['id'],
        #     source=row['source_id'],
        #     external_id=row['external_id'],
        #     invoice_id='1',
        #     is_reconciled=False,
        # )

        # with Session(new_spend_db_engine) as session:
        #     session.add(transaction)
        #     session.commit()

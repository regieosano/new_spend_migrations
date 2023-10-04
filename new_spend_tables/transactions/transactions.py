import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from transactions_class import Transactions
from _database.engine_db import engine as new_spend_db_engine


source_csv_file = "new_spend_tables/transactions/legacy/dump/transaction_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

transaction_data = pd.read_csv(source_csv_file)

LENGTH_OF_TRANSACTION_DATA = len(transaction_data)

record = transaction_data.to_dict()

for i in range(LENGTH_OF_TRANSACTION_DATA):
    transaction = Transactions(
        id=record['id'][i],
        source=record['source_id'][i],
        external_id=record['external_id'][i],
        invoice_id=record['invoice_id'][i],
        is_reconciled=False,
    )

    with Session(new_spend_db_engine) as session:
        session.add(transaction)
        session.commit()


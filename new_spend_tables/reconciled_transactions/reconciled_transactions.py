import csv
from sqlalchemy.orm import Session, sessionmaker
from reconciled_transactions_class import ReconciledTransactions
from _database.engine_db import engine
from _database.engine_db_legacy import engine as engine_legacy
from new_spend_tables.transactions.legacy.transaction_class_legacy import Transaction

source_csv_file_budget_trans = "new_spend_tables/budget_transactions/legacy/dump/budget_transaction_data_dump.csv"
source_csv_file_income_budget_trans = "new_spend_tables/income_budget_transactions/legacy/dump/income_budget_transaction_data_dump.csv"

session_pool = sessionmaker(engine)
session_pool_legacy = sessionmaker(engine_legacy)

# budget_transactions
with open(source_csv_file_budget_trans, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    existing_trans_ids = []
    reconciled_transactions = []
    for row in reader:
        if row['transaction_id'] in existing_trans_ids:
            continue
        existing_trans_ids.append(row['transaction_id'])
        transaction_amount = 0
        with Session(engine_legacy) as session_legacy:
            transaction = session_legacy.query(Transaction).filter_by(id=row['transaction_id']).first()
            transaction_amount = transaction.amount
        reconciled_transaction = ReconciledTransactions(
            id=row['budget_id'],
            payment_id=str(row['transaction_id']),
            amount=transaction_amount,
            type="expense",
            created_at=row['created_at'],
            # updated_at=row['updated_at'],
            # budget_category_type=None,
        )
        reconciled_transactions.append(reconciled_transaction)

    with Session(engine) as session:
        session.add_all(reconciled_transactions)
        session.commit()
        session.close()

# income_budget_transactions
with open(source_csv_file_income_budget_trans, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    existing_trans_ids = []
    reconciled_transactions = []
    for row in reader:
        if row['transaction_id'] in existing_trans_ids:
            continue
        existing_trans_ids.append(row['transaction_id'])
        transaction_amount = 0
        with Session(engine_legacy) as session_legacy:
            transaction = session_legacy.query(Transaction).filter_by(id=row['transaction_id']).first()
            transaction_amount = transaction.amount
        reconciled_transaction = ReconciledTransactions(
            id=row['budget_id'],
            payment_id=str(row['transaction_id']),
            amount=transaction_amount,
            type="income",
            created_at=row['created_at'],
            # updated_at=row['updated_at'],
            # budget_category_type=None,
        )
        reconciled_transactions.append(reconciled_transaction)

    with Session(engine) as session:
        session.add_all(reconciled_transactions)
        session.commit()
        session.close()
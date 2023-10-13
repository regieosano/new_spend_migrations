import csv
from sqlalchemy.orm import Session, sessionmaker
from reconciled_transactions_class import ReconciledTransactions
from _database.engine_db import engine
from _database.engine_db_legacy import engine as engine_legacy
from new_spend_tables.transactions.legacy.transaction_class_legacy import Transaction
from _dummy.dummy_data_values import DUMMY_VALID_DATE
from cuid import cuid
import json

source_csv_file_budget_trans = "new_spend_tables/budget_transactions/legacy/dump/budget_transaction_data_dump.csv"
source_csv_file_income_budget_trans = "new_spend_tables/income_budget_transactions/legacy/dump/income_budget_transaction_data_dump.csv"
source_csv_file_invoice_trans = "new_spend_tables/invoice_transactions/legacy/dump/invoice_transaction_data_dump.csv"

session_pool = sessionmaker(engine)
session_pool_legacy = sessionmaker(engine_legacy)

reconciled_transactions_id_lookup = {}

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
        id = 'spdrtx_%s' % cuid()
        reconciled_transactions_id_lookup[row['budget_id']] = id
        reconciled_transaction = ReconciledTransactions(
            id=id,
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
        id = 'spdrtx_%s' % cuid()
        reconciled_transactions_id_lookup[row['budget_id']] = id
        reconciled_transaction = ReconciledTransactions(
            id=id,
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

# invoice_budget_transactions
with open(source_csv_file_invoice_trans, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    existing_trans_ids = {}
    reconciled_transactions = []

    for row in reader:
        with Session(engine) as session:
            is_in_reconciled_transactions = session.query(ReconciledTransactions).filter_by(payment_id=row['transaction_id']).first()
            if is_in_reconciled_transactions:
                continue
        transaction_amount = 0
        transaction_date = ''
        transaction_type = 'income'
        with Session(engine_legacy) as session_legacy:
            transaction = session_legacy.query(Transaction).filter_by(id=row['transaction_id']).first()
            transaction_amount = transaction.amount
            transaction_date = transaction.created_at
            if transaction.type == "refund":
                transaction_type = "expense"
        if row['transaction_id'] in existing_trans_ids:
            session.query(ReconciledTransactions).filter(ReconciledTransactions.payment_id==row['transaction_id'])\
                .update({'amount': ReconciledTransactions.amount + transaction_amount})
            session.commit()
            continue

        existing_trans_ids[row['transaction_id']] = transaction_amount
        
        id = 'spdrtx_%s' % cuid()
        reconciled_transactions_id_lookup[row['id']] = id
        reconciled_transaction = ReconciledTransactions(
            id=id,
            payment_id=str(row['transaction_id']),
            amount=transaction_amount,
            # decide if income or expense
            type=transaction_type,
            created_at=transaction_date,
            # updated_at=row['updated_at'],
            # budget_category_type=None,
        )
        reconciled_transactions.append(reconciled_transaction)

    with Session(engine) as session:
        session.add_all(reconciled_transactions)
        session.commit()
        session.close()

with open('new_spend_tables/reconciled_transactions/idlookup/reconciled_transactions_id_lookup.json', 'w+') as id_lookup_file:
    json.dump(reconciled_transactions_id_lookup, id_lookup_file)
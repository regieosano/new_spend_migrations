import csv
from sqlalchemy.orm import Session, sessionmaker
from budget_transactions_class import Budget_Transactions
from _database.engine_db import engine
from cuid import cuid
import json

reconciled_transactions_id_lookup_file = open(
    'new_spend_tables/reconciled_transactions/idlookup/reconciled_transactions_id_lookup.json')
reconciled_transactions_id_lookup = json.load(reconciled_transactions_id_lookup_file)

budget_item_id_lookup_file = open(
    'new_spend_tables/budget_items/idlookup/budget_items_id_lookup.json')
budget_item_id_lookup = json.load(budget_item_id_lookup_file)


expense_source_csv_file = "new_spend_tables/budget_transactions/legacy/dump/budget_transaction_data_dump.csv"
income_source_csv_file = "new_spend_tables/income_budget_transactions/legacy/dump/income_budget_transaction_data_dump.csv"

session_pool = sessionmaker(engine)

with open(expense_source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            budget_transaction = Budget_Transactions(
                id=row['id'],
                transaction_id=reconciled_transactions_id_lookup[row['budget_id']],
                budget_item_id=budget_item_id_lookup[row['budget_id']],
                amount=row['amount'],
            )

            with Session(engine) as session:
                session.add(budget_transaction)
                session.commit()
        except:
            continue

with open(income_source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            budget_transaction = Budget_Transactions(
                id=row['id'],
                transaction_id=reconciled_transactions_id_lookup[row['budget_id']],
                budget_item_id=budget_item_id_lookup[row['budget_id']],
                amount=row['amount'],
            )

            with Session(engine) as session:
                session.add(budget_transaction)
                session.commit()
        except:
            continue

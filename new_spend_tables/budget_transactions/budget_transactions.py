import csv
from sqlalchemy.orm import Session, sessionmaker
from budget_transactions_class import Budget_Transactions
from _database.engine_db import engine

expense_source_csv_file = "new_spend_tables/budget_transactions/legacy/dump/budget_transaction_data_dump.csv"
income_source_csv_file = "new_spend_tables/income_budget_transactions/legacy/dump/income_budget_transaction_data_dump.csv"

session_pool = sessionmaker(engine)

with open(expense_source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        budget_transaction = Budget_Transactions(
            id=row['budget_id'],
            transaction_id=row['transaction_id'],
            budget_item_id=row['budget_id'],
            amount=row['amount'],
        )

        with Session(engine) as session:
            session.add(budget_transaction)
            session.commit()

with open(income_source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        budget_transaction = Budget_Transactions(
            id=row['budget_id'],
            transaction_id=row['transaction_id'],
            budget_item_id=row['budget_id'],
            amount=row['amount'],
        )

        with Session(engine) as session:
            session.add(budget_transaction)
            session.commit()

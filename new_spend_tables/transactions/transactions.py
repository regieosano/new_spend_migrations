import csv

from sqlalchemy.orm import Session, sessionmaker
from transactions_class import Transactions
from _database.engine_db import engine


source_csv_file = "transactions/transaction_test_data_dump.csv"


session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    pass

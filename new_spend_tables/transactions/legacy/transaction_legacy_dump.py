import csv
from transaction_class_legacy import Transaction
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

transactions_id_lookup_file = open(
    'new_spend_tables/transactions/transactions_id_lookup.json')

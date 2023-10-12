import csv
from sqlalchemy.orm import Session, sessionmaker
from invoice_transactions_class import InvoiceTransactions
from new_spend_tables.reconciled_transactions.reconciled_transactions_class import ReconciledTransactions
from _database.engine_db import engine
import json

source_csv_file = "new_spend_tables/invoice_transactions/legacy/dump/invoice_transaction_data_dump.csv"

reconciled_transactions_id_lookup_file = open(
    'new_spend_tables/reconciled_transactions/idlookup/reconciled_transactions_id_lookup.json')
reconciled_transactions_id_lookup = json.load(reconciled_transactions_id_lookup_file)

invoice_id_lookup_file = open(
    'new_spend_tables/invoices/idlookup/invoices_id_lookup.json')
invoice_id_lookup = json.load(invoice_id_lookup_file)

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    invoice_transactions = []
    for row in reader:
        with Session(engine) as session:
            is_in_reconciled_transactions = session.query(ReconciledTransactions).filter_by(payment_id=row['transaction_id']).first()
            if is_in_reconciled_transactions:
                continue
        invoice_transaction = InvoiceTransactions(
            id=row['id'],
            transaction_id=reconciled_transactions_id_lookup[row['invoice_id']],
            invoice_id=invoice_id_lookup[row['invoice_id']],
            amount=row['amount'],
        )
        invoice_transactions.append(invoice_transaction)
        if i > 10:
            break

    with Session(engine) as session:
        session.add_all(invoice_transactions)
        session.commit()
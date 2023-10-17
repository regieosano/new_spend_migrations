import csv
from sqlalchemy.orm import Session, sessionmaker
from invoice_transactions_class import InvoiceTransactions
from new_spend_tables.reconciled_transactions.reconciled_transactions_class import ReconciledTransactions
from _database.engine_db import engine
from new_spend_tables.invoices.invoices_class import Invoices
from new_spend_tables.transactions.legacy.transaction_class_legacy import Transaction
from _database.engine_db_legacy import engine as engine_legacy
from _dummy.dummy_data_values import DUMMY_VALID_DATE
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
    # i = 0
    for row in reader:
        # i += 1
        # with Session(engine) as session:
        #     is_in_reconciled_transactions = session.query(ReconciledTransactions).filter_by(payment_id=row['transaction_id']).first()
        #     if is_in_reconciled_transactions:
        #         continue
        try:
            invoice_transaction = InvoiceTransactions(
                id=row['id'],
                transaction_id=reconciled_transactions_id_lookup[row['invoice_id']],
                invoice_id=invoice_id_lookup[row['invoice_id']],
                amount=row['amount'],
            )

            is_refunded = False
            refund_date = DUMMY_VALID_DATE
            discount_amount = 0

            # invoice recode updates
            with Session(engine_legacy) as session_legacy:
                transaction = session_legacy.query(Transaction).filter_by(id=row['transaction_id']).first()
                if transaction.type == 'refund':
                    is_refunded = True
                refund_date = transaction.created_at
                discount_amount = transaction.discount
                with Session(engine) as session:
                    session.query(Invoices).update({
                        'is_refunded': is_refunded,
                        'refund_date': refund_date,
                        'discount_amount': discount_amount,
                    })
                    session.commit()

            with Session(engine) as session:
                session.add(invoice_transaction)
                session.commit()
        except:
            continue
        # if i >= 10000:
        #     break
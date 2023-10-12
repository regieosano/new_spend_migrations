import csv
from zipfile import ZipFile
from new_spend_tables.invoice_transactions.legacy.invoice_transaction_class import InvoiceTransaction
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine as spend_dev_engine
from cuid import cuid
import json

session_pool = sessionmaker(spend_dev_engine)

with open('new_spend_tables/invoice_transactions/legacy/dump/invoice_transaction_data_dump.csv', 'w+', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'invoice_id',
        'amount',
        'transaction_id',
        'fee',
        'revenue',
        'discount',
    ])
    id_lookup = {}
    with Session(spend_dev_engine) as session:
        records = session.query(InvoiceTransaction).all()
        for col in records:
            id = 'spdbtr_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.invoice_id,
                col.amount,
                col.transaction_id,
                col.fee,
                col.revenue,
                col.discount,
            ])
        with open('new_spend_tables/invoice_transactions/idlookup/invoice_transactions_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/invoice_transactions/zipped/invoice_transaction_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/invoice_transactions/legacy/dump/invoice_transaction_data_dump.csv')
    zipObj.write(
        'new_spend_tables/invoice_transactions/idlookup/invoice_transactions_id_lookup.json')
    zipObj.close()

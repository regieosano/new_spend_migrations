import csv
from zipfile import ZipFile
from budget_transaction_class_legacy import Budget_Transaction
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine as spend_dev_engine
from cuid import cuid
import json

session_pool = sessionmaker(spend_dev_engine)

with open('new_spend_tables/budget_transactions/legacy/dump/budget_transaction_data_dump.csv', 'w+', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'budget_id',
        'transaction_id',
        'amount',
        'created_at',
        'updated_at',
    ])
    id_lookup = {}
    with Session(spend_dev_engine) as session:
        records = session.query(Budget_Transaction).all()
        for col in records:
            id = 'spdbtr_%s' % cuid()
            id_lookup[col.budget_id] = id
            outcsv.writerow([
                id,
                col.transaction_id,
                col.amount,
                col.created_at,
                col.updated_at,
            ])
        with open('new_spend_tables/budget_transactions/idlookup/budget_transactions_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/budget_transactions/zipped/budget_transaction_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/budget_transactions/legacy/dump/budget_transaction_data_dump.csv')
    zipObj.write(
        'new_spend_tables/budget_transactions/idlookup/budget_transactions_id_lookup.json')
    zipObj.close()

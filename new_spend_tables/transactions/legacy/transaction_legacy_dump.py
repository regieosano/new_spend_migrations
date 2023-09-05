import csv
from zipfile import ZipFile
from transaction_class_legacy import Transaction
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/transactions/transaction_test_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'source_id',
        'type',
        'method',
        'check_no',
        'amount',
        'fee',
        'revenue',
        'cost',
        'status',
        'reason',
        'settled_at',
        'external_id',
        'paystand_event_id',
        'created_at',
        'updated_at',
        'entry',
        'org_id',
        'note',
        'discount',
        'destination_id',
        'external',
        'source_balance',
        'idempotency_key',
        'debit_card_id',
        'merchant',
        'returned',
        'destination_balance',
        'return_fee',
        'disputed',
        'initiator_id',
        'notified_on',
        'memo',
        'destination_note',
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Transaction).all()
        for col in records:
            id = 'spdtra_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.source_id,
                col.type,
                col.method,
                col.check_no,
                col.amount,
                col.fee,
                col.revenue,
                col.cost,
                col.status,
                col.reason,
                col.settled_at,
                col.external_id,
                col.paystand_event_id,
                col.created_at,
                col.updated_at,
                col.entry,
                col.org_id,
                col.note,
                col.discount,
                col.destination_id,
                col.external,
                col.source_balance,
                col.idempotency_key,
                col.debit_card_id,
                col.merchant,
                col.returned,
                col.destination_balance,
                col.return_fee,
                col.disputed,
                col.initiator_id,
                col.notified_on,
                col.memo,
                col.destination_note,
            ])
        with open('new_spend_tables/transactions/transaction_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/transactions/transaction_csv_json_.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/transactions/transaction_test_data_dump.csv')
    zipObj.write('new_spend_tables/transactions/transaction_id_lookup.json')
    zipObj.close()

import csv
from zipfile import ZipFile
from invoice_class_legacy import Invoice
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/invoices/legacy/dump/invoice_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'invoice_id',
        'team_player_id',
        'description',
        'due_date',
        'optional',
        'opted_in',
        'stopped',
        'last_parent_notification_date',
        'last_parent_notification_age',
        'note',
        'payment_schedule_invoice_id',
        'payment_method_id',
        'amount_due',
        'reason',
        'status',
        'cc_fee_base',
        'cc_fee_pct',
        'app_fee_base',
        'app_fee_pct',
        'created_at',
        'updated_at',
        'penalty',
        'paid',
        'pending',
        'credit',
        'memo',
        'budget_item_id'
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Invoice).all()
        for col in records:
            id = 'spdinv_%s' % cuid()
            id_lookup[col.invoice_id] = id
            outcsv.writerow([
                id,
                col.team_player_id,
                col.description,
                col.due_date,
                col.optional,
                col.opted_in,
                col.stopped,
                col.last_parent_notification_date,
                col.last_parent_notification_age,
                col.note,
                col.payment_schedule_invoice_id,
                col.payment_method_id,
                col.amount_due,
                col.reason,
                col.status,
                col.cc_fee_base,
                col.cc_fee_pct,
                col.app_fee_base,
                col.app_fee_pct,
                col.created_at,
                col.updated_at,
                col.penalty,
                col.paid,
                col.pending,
                col.credit,
                col.memo,
                col.budget_item_id
            ])
        with open('new_spend_tables/invoices/idlookup/invoices_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/invoices/zipped/invoice_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/invoices/legacy/dump/invoice_data_dump.csv')
    zipObj.write('new_spend_tables/invoices/idlookup/invoices_id_lookup.json')
    zipObj.close()

import csv
from zipfile import ZipFile
from payment_schedule_invoice_class_legacy import PaymentScheduleInvoice
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine as spend_dev_engine
from cuid import cuid
import json

session_pool = sessionmaker(spend_dev_engine)

with open('new_spend_tables/payment_schedule_invoices/legacy/dump/payment_schedule_invoice_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    column_headers = [
        'schedule_invoice_id',
        'description',
        'due_date',
        'optional',
        'state',
        'note',
        'amount_due',
        'team_id',
        'season_id',
        'budget_item_id',
    ]
    outcsv.writerow(column_headers)
    id_lookup = {}

    with open(
            'new_spend_tables/payment_schedule_invoices/legacy/dump/payment_schedule_invoice_bad_data.csv',
            'w+',
            encoding='UTF-8',
            newline=''
        ) as bad_data_file:
        bad_data_file_csv = csv.writer(bad_data_file, delimiter=',')
        bad_data_file_csv.writerow(column_headers)

        with Session(spend_dev_engine) as session:
            records = session.query(PaymentScheduleInvoice).all()
            for col in records:
                id = 'spdpsi_%s' % cuid()
                id_lookup[col.schedule_invoice_id] = id
                row = [
                    id,
                    col.description,
                    col.due_date,
                    col.optional,
                    col.state,
                    col.note,
                    col.amount_due,
                    col.team_id,
                    col.season_id,
                    col.budget_item_id,
                ]
                if not col.season_id or not col.team_id or not col.budget_item_id:
                        bad_data_file_csv.writerow(row)
                        # to skip writing rows that are bad data in the actual dump uncomment the line below
                        # continue
                outcsv.writerow(row)
            with open('new_spend_tables/payment_schedule_invoices/idlookup/payment_schedule_invoices_id_lookup.json', 'w+') as id_lookup_file:
                json.dump(id_lookup, id_lookup_file)
        bad_data_file.close()
    outfile.close()

with ZipFile('new_spend_tables/payment_schedule_invoices/zipped/payment_schedule_invoice_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/payment_schedule_invoices/legacy/dump/payment_schedule_invoice_data_dump.csv')
    zipObj.write(
        'new_spend_tables/payment_schedule_invoices/idlookup/payment_schedule_invoices_id_lookup.json')
    zipObj.close()
import csv
from invoice_class_legacy import Invoice
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine

session_pool = sessionmaker(engine)

with open('new_spend_tables/invoices/invoice_test_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
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
    with Session(engine) as session:
        records = session.query(Invoice).all()
        for col in records:
            outcsv.writerow([
                col.invoice_id,
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

    outfile.close()

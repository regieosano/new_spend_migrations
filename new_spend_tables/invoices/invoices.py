import csv
from cuid import cuid
from sqlalchemy.orm import Session, sessionmaker
from invoices_class import Invoices
from _database.engine_db import engine

source_csv_file = "new_spend_tables/invoices/legacy/dump/invoice_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        created_at_value = '2023-01-01 00:00:00.000000' if row['created_at'] == '' else row['created_at']
        updated_at_value = '2023-01-01 00:00:00.000000' if row['updated_at'] == '' else row['updated_at']
        due_date_value = '2023-01-01 00:00:00.000000' if row['due_date'] == '' else row['due_date']
        last_notification_date_value = '2023-01-01 00:00:00.000000' if row[
            'last_parent_notification_date'] == '' else row['last_parent_notification_date']
        invoice = Invoices(
            id=row['invoice_id'],
            paid=False,
            amount=row['amount_due'],
            note=row['note'],
            paid_date='2023-01-01 00:00:00.000000',
            last_notification_date=last_notification_date_value,
            notification_attempts=5,
            last_notification_id='Test Id',
            description=row['description'],
            balance_due=row['amount_due'],
            is_optional=False,
            opted_in=False,
            created_at=created_at_value,
            updated_at=updated_at_value,
            due_date=due_date_value,
            payment_schedule_invoice_id=row['payment_schedule_invoice_id'],
            group_roster_id=row['team_player_id'],
            budget_item_id='1255',
            payment_method_source='',
            payment_method_id=row['payment_method_id'],
            is_refunded=False,
            refund_date='2023-01-01 00:00:00.000000',
            is_auto_pay_authorized=False,
            is_archived=False,
        )

        with Session(engine) as session:
            session.add(invoice)
            session.commit()

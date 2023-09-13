import csv
from cuid import cuid
from sqlalchemy.orm import Session, sessionmaker
from invoices_class import Invoices
from _database.engine_db import engine

source_csv_file = "new_spend_tables/invoices/invoice_test_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        invoice = Invoices(
            id=row['invoice_id'],
            paid=True,
            amount=row['amount_due'],
            note=row['note'],
            paid_date=row['due_date'],
            last_notification_date=row['last_parent_notification_date'],
            notification_attempts=5,
            last_notification_id='Test Id',
            description=row['description'],
            balance_due=row['amount_due'],
            is_optional=False,
            opted_in=False,
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            due_date=row['due_date'],
            payment_schedule_invoice_id=row['payment_schedule_invoice_id'],
            group_roster_id=row['team_player_id'],
            budget_item_id='1255',
        )

        with Session(engine) as session:
            session.add(invoice)
            session.commit()

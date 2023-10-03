import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from payment_schedule_invoices_class import PaymentScheduleInvoices
from _lookup.lookup_tables import group_id_lookup, budget_item_id_lookup, season_id_lookup
from _dummy.dummy_data_values import DUMMY_VALID_BUDGET_ITEM_ID, DUMMY_VALID_GROUP_ID, DUMMY_VALID_SEASON_ID 
from _database.engine_db import engine as new_spend_db_engine

source_csv_file = "new_spend_tables/payment_schedule_invoices/legacy/dump/payment_schedule_invoice_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

payment_schedule_invoice_data = pd.read_csv(source_csv_file)

LENGTH_OF_PAYMENT_SCHEDULE_INVOICE_DATA = len(payment_schedule_invoice_data)

record = payment_schedule_invoice_data.to_dict()

for i in range(LENGTH_OF_PAYMENT_SCHEDULE_INVOICE_DATA):
    try:
        group_id_value = DUMMY_VALID_GROUP_ID if pd.isna(group_id_lookup[record['team_id'][i]]) else group_id_lookup[record['team_id'][i]]
    except KeyError:
        group_id_value = DUMMY_VALID_GROUP_ID 
    try:       
        season_id_value = DUMMY_VALID_SEASON_ID if pd.isna(season_id_lookup[str(record['season_id'][i])]) else season_id_lookup[str(record['season_id'][i])]
    except KeyError:
        season_id_value = DUMMY_VALID_GROUP_ID    
    try:
        budget_item_id_value = DUMMY_VALID_BUDGET_ITEM_ID if pd.isna(record['budget_item_id'][i]) else budget_item_id_lookup[str(int(record['budget_item_id'][i]))]
    except KeyError:
        budget_item_id_value = DUMMY_VALID_BUDGET_ITEM_ID
    payment_schedule_invoice = PaymentScheduleInvoices(
        id=record['schedule_invoice_id'][i],
        description=record['description'][i],
        note=record['note'][i],
        amount_due=record['amount_due'][i],
        due_date=record['due_date'][i],
        is_optional=record['optional'][i],
        status=record['state'][i],
        group_id=group_id_value,
        season_id=season_id_value,
        budget_item_id=budget_item_id_value,
        is_archived=False,
        last_published_state=''
    )

    with Session(new_spend_db_engine) as session:
        session.add(payment_schedule_invoice)
        session.commit()
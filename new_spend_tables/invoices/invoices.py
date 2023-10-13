import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from invoices_class import Invoices
from _database.engine_db import engine as new_spend_db_engine
from _lookup.lookup_tables import budget_item_id_lookup, payment_schedule_invoice_id_lookup, group_id_lookup 
from _dummy.dummy_data_values import DUMMY_VALID_NOTIFICATION_ID, DUMMY_VALID_GROUP_ROSTER_ID, DUMMY_VALID_DATE, DUMMY_VALID_BUDGET_ITEM_ID, DUMMY_VALID_PAYMENT_SCHED_INVC_ID
from new_spend_tables.transactions.legacy.transaction_class_legacy import Transaction
from new_spend_tables.credit_memo.credit_memo_class import CreditMemo
from _database.engine_db_legacy import engine as engine_legacy
from cuid import cuid

source_csv_file = "new_spend_tables/invoices/legacy/dump/invoice_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

invoice_data = pd.read_csv(source_csv_file)

LENGTH_OF_INVOICE_DATA = len(invoice_data)

record = invoice_data.to_dict()

for i in range(LENGTH_OF_INVOICE_DATA):
    created_at_value = DUMMY_VALID_DATE if pd.isna(record['created_at'][i]) else record['created_at'][i]
    updated_at_value = DUMMY_VALID_DATE if pd.isna(record['updated_at'][i]) else record['updated_at'][i]
    due_date_value = DUMMY_VALID_DATE if pd.isna(record['due_date'][i]) else record['due_date'][i]
    try:
     last_notification_date_value = DUMMY_VALID_DATE if pd.isna(
        record['last_parent_notification_date'][i]) else record['last_parent_notification_date'][i]
    except KeyError:
        last_notification_date_value = DUMMY_VALID_DATE
    try:
        budget_item_id_value = DUMMY_VALID_BUDGET_ITEM_ID if pd.isna(budget_item_id_lookup[str(record['budget_item_id'][i])]) else budget_item_id_lookup[str(record['budget_item_id'][i])]
    except KeyError:
        budget_item_id_value = DUMMY_VALID_BUDGET_ITEM_ID
    try:
        group_roster_id_value = DUMMY_VALID_GROUP_ROSTER_ID if pd.isna(group_id_lookup[record['team_player_id'][i]]) else group_id_lookup[record['team_player_id'][i]] 
    except KeyError:
        group_roster_id_value = DUMMY_VALID_GROUP_ROSTER_ID        
    try:
        payment_schedule_invoice_id_value = DUMMY_VALID_BUDGET_ITEM_ID if pd.isna(payment_schedule_invoice_id_lookup[record['payment_schedule_invoice_id'][i]]) else payment_schedule_invoice_id_lookup[record['payment_schedule_invoice_id'][i]]  
    except KeyError:
        payment_schedule_invoice_id_value = DUMMY_VALID_PAYMENT_SCHED_INVC_ID
    
    is_refunded = False
    refund_date = DUMMY_VALID_DATE
    discount_amount = 0

    with Session(engine_legacy) as session_legacy:
        transaction = session_legacy.query(Transaction).filter_by(id=record['transaction_id'][i]).first()
        if transaction.type == 'refund':
            is_refunded = True
        refund_date = transaction.created_at
        discount_amount = transaction.discount
    
    invoice = Invoices(
        id=record['invoice_id'][i],
        paid=False,
        amount=record['amount_due'][i],
        note=record['note'][i],
        paid_date=DUMMY_VALID_DATE,
        last_notification_date=last_notification_date_value,
        notification_attempts=0,
        last_notification_id=DUMMY_VALID_NOTIFICATION_ID,
        description=record['description'][i],
        balance_due=record['amount_due'][i],
        is_optional=False,
        opted_in=False,
        created_at=created_at_value,
        updated_at=updated_at_value,
        due_date=due_date_value,
        payment_schedule_invoice_id=payment_schedule_invoice_id_value,
        group_roster_id=group_roster_id_value,
        budget_item_id=budget_item_id_value,
        payment_method_source='',
        payment_method_id=record['payment_method_id'][i],
        is_refunded=is_refunded,
        refund_date=refund_date,
        is_auto_pay_authorized=False,
        is_archived=False,
        discount_amount=discount_amount,
        penalty_amount=record['penalty'][i],
    )

    with Session(new_spend_db_engine) as session:
        session.add(invoice)
        session.commit()
    
    # credit memo
    if float(record['credit'][i]):
        credit_memo_id = 'spdcdtm_%s' % cuid()
        credit_memo = CreditMemo(
            id=credit_memo_id,
            correlationId=cuid(),
            note=record['memo'][i],
            dateToApply=record['due_date'][i],
            creditApplied=record['credit'][i],
            creditAmount=record['credit'][i],
            createdAt=record['memdue_dateo'][i],
            createdByUserId='generic-user-from-legacy',
            isArchived=False,
            invoiceId=record['invoice_id'][i],
        )




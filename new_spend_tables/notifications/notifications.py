import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from notifications_class import Notifications
from _database.engine_db import engine as new_spend_db_engine
from _dummy.dummy_data_values import DUMMY_VALID_DATE

source_csv_file = "new_spend_tables/notifications/legacy/dump/notifications_data_dump.csv"

session_pool = sessionmaker(new_spend_db_engine)

notification_data = pd.read_csv(source_csv_file)

LENGTH_OF_NOTIFICATION_DATA = len(notification_data)

record = notification_data.to_dict()

for i in range(LENGTH_OF_NOTIFICATION_DATA):
    try:
        created_at_value = DUMMY_VALID_DATE if pd.isna(record['created_at'][i]) else record['created_at'][i]
    except:
        created_at_value = DUMMY_VALID_DATE
    try:       
        updated_at_value = DUMMY_VALID_DATE if pd.isna(record['updated_at'][i]) else record['updated_at'][i]
    except:
        updated_at_value = DUMMY_VALID_DATE   
     
    notification = Notifications(
        id=record['id'][i],
        past_due=record['past_due'][i],
        failed_payment=record['failed_payment'][i],
        created_at=created_at_value,
        updated_at=updated_at_value,
    )

    with Session(new_spend_db_engine) as session:
        session.add(notification)
        session.commit()
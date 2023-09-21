import csv
import uuid

from sqlalchemy.orm import Session, sessionmaker
from organizations_class import Organizations
from _database.engine_db import engine

source_csv_file = "new_spend_tables/organizations/legacy/dump/organization_data_dump.csv"

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        verified_value = True if row['verified'] == 'TRUE' else False
        organization = Organizations(
            id=row['id'],
            legal_name=row['legal_name'],
            email=row['email'],
            phone=row['phone'],
            # verify street
            street='',
            city=row['city'],
            state=row['state'],
            zip=row['zip'],
            website=row['website'],
            logo=row['logo_url'],
            is_verified=verified_value,
            # verify user_id
            user_id='',
            # verify org_id
            org_id=uuid.uuid4(),
            external_id=uuid.uuid4(),
            account_id=row['account_id'],
            spend_base_fee=row['app_fee_base'],
            # verify the following
            spend_percent=0.0,
            card_base_fee=0,
            card_percent=0.0,
            ach_base_fee=0,
            ach_percent=0.0
        )

        with Session(engine) as session:
            session.add(organization)
            session.commit()

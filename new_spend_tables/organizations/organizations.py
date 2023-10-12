import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from organizations_class import Organizations
from _database.engine_db import engine
from datetime import datetime
from cuid import cuid

source_csv_file = "new_spend_tables/organizations/legacy/dump/organization_data_dump.csv"

session_pool = sessionmaker(engine)

organization_data = pd.read_csv(source_csv_file)

LENGTH_OF_ORGANIZATION_DATA = len(organization_data)

record = organization_data.to_dict()

for i in range(LENGTH_OF_ORGANIZATION_DATA):
    verified_value = True if record['verified'][i] == 'TRUE' else False
    external_id_value = cuid() if pd.isna(record[
        'external_id'][i]) else record['external_id'][i]
    organization = Organizations(
        id=record['id'][i],
        legal_name=record['legal_name'][i],
        email=record['email'][i],
        phone=record['phone'][i],
        # verify street
        street='',
        city=record['city'][i],
        state=record['state'][i],
        zip=record['zip'][i],
        website=record['website'][i],
        logo=record['logo_url'][i],
        is_verified=verified_value,
        # verify user_id
        user_id='',
        # verify org_id
        org_id=f'NULL {cuid()}',
        external_id=external_id_value,
        account_id=record['account_id'][i],
        spend_base_fee=record['app_fee_base'][i],
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

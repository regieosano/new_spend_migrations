import csv
from sqlalchemy.orm import Session, sessionmaker
from new_spend_tables.agreements.agreements_class import Agreements
from _database.engine_db import engine
import json

source_csv_file = "new_spend_tables/agreements/legacy/dump/agreement_data_dump.csv"

organization_id_lookup_file = open(
    'new_spend_tables/organizations/idlookup/organization_id_lookup.json')
organization_id_lookup = json.load(organization_id_lookup_file)

session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    agreements = []
    for row in reader:
        agreement = Agreements(
            id=row['id'],
            org_id=organization_id_lookup[row['org_id']],
            name=row['name'],
            content=row['content'],
            is_active=row['status'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
        )
        agreements.append(agreement)

    with Session(engine) as session:
        session.add_all(agreements)
        session.commit()
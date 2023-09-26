import csv
from zipfile import ZipFile
from team_class_legacy import Team
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/groups/legacy/dump/group_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'team_id',
        'team_name',
        'sport',
        'archived',
        'app_fee_base',
        'app_fee_pct',
        'org_id',
        'payment_method_id',
        'bank_enabled',
        'agreement_enabled',
        'agreement_id',
        'active_date',
        'created_at',
        'inactive_date',
        'updated_at',
        'account_id',
        'external_doc_id',
        'external_id',
        'synapse_verified',
        'synapse_flagged',
        'synapse_watchlists',
        'synapse_doc_status',
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Team).all()
        for col in records:
            id = 'spdgrp_%s' % cuid()
            id_lookup[col.team_id] = id
            outcsv.writerow([
                id,
                col.team_name,
                col.sport,
                col.archived,
                col.app_fee_base,
                col.app_fee_pct,
                col.org_id,
                col.payment_method_id,
                col.bank_enabled,
                col.agreement_enabled,
                col.agreement_id,
                col.active_date,
                col.created_at,
                col.inactive_date,
                col.updated_at,
                col.account_id,
                col.external_doc_id,
                col.external_id,
                col.synapse_verified,
                col.synapse_flagged,
                col.synapse_watchlists,
                col.synapse_doc_status,
            ])
        with open('new_spend_tables/groups/idlookup/groups_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/groups/zipped/group_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/groups/legacy/dump/group_data_dump.csv')
    zipObj.write(
        'new_spend_tables/groups/idlookup/groups_id_lookup.json')
    zipObj.close()

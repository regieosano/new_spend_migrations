import csv
from organization_class_legacy import Organization
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine

session_pool = sessionmaker(engine)

# MISSING FIELDS (Present in legacy but not in new spend)
# address1
# address2
# payment_method_id
# hash
# nickname
# type
# sport
# statement_descriptor
# app_fee_pct
# cc_fee_base
# approved
# strict
# notification
# status
# reason
# paystand_id
# paystand_bank_id
# paystand_event_id
# created_at
# updated_at
# team_banks_enabled
# agreement_enabled
# sales_id
# app_bank_id
# external_doc_id
# synapse_verified
# notify_upcoming_everyone
# synapse_flagged
# synapse_watchlists
# synapse_doc_status
# subscription_team_fee
# subscription_plan
# bank_2fa_completed
# cip
# external_transfer_out_enabled

with open('organizations/organization_test_data_dump.csv', 'w', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'payment_method_id',
        'hash',
        'legal_name',
        'nickname',
        'type',
        'sport',
        'email',
        'phone',
        'website',
        'logo_url',
        'address1',
        'address2',
        'city',
        'state',
        'zip',
        'statement_descriptor',
        'app_fee_pct',
        'app_fee_base',
        'cc_fee_pct',
        'cc_fee_base',
        'approved',
        'verified',
        'strict',
        'notification',
        'status',
        'reason',
        'paystand_id',
        'paystand_bank_id',
        'paystand_event_id',
        'created_at',
        'updated_at',
        'team_banks_enabled',
        'agreement_enabled',
        'sales_id',
        'app_bank_id',
        'external_id',
        'external_doc_id',
        'account_id',
        'synapse_verified',
        'notify_upcoming_everyone',
        'synapse_flagged',
        'synapse_watchlists',
        'synapse_doc_status',
        'subscription_team_fee',
        'subscription_plan',
        'bank_2fa_completed',
        'cip',
        'external_transfer_out_enabled'
    ])
    with Session(engine) as session:
        records = session.query(Organization).all()
        for col in records:
            outcsv.writerow([
                col.id,
                col.payment_method_id,
                col.hash,
                col.legal_name,
                col.nickname,
                col.type,
                col.sport,
                col.email,
                col.phone,
                col.website,
                col.logo_url,
                col.address1,
                col.address2,
                col.city,
                col.state,
                col.zip,
                col.statement_descriptor,
                col.app_fee_pct,
                col.app_fee_base,
                col.cc_fee_pct,
                col.cc_fee_base,
                col.approved,
                col.verified,
                col.strict,
                col.notification,
                col.status,
                col.reason,
                col.paystand_id,
                col.paystand_bank_id,
                col.paystand_event_id,
                col.created_at,
                col.updated_at,
                col.team_banks_enabled,
                col.agreement_enabled,
                col.sales_id,
                col.app_bank_id,
                col.external_id,
                col.external_doc_id,
                col.account_id,
                col.synapse_verified,
                col.notify_upcoming_everyone,
                col.synapse_flagged,
                col.synapse_watchlists,
                col.synapse_doc_status,
                col.subscription_team_fee,
                col.subscription_plan,
                col.bank_2fa_completed,
                col.cip,
                col.external_transfer_out_enabled
            ])

    outfile.close()

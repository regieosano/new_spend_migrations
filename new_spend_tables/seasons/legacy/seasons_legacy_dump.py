import csv
from seasons_class_legacy import Seasons
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine

session_pool = sessionmaker(engine)

with open('new_spend_tables/seasons/season_test_data_dump.csv', 'w', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'created_at',
        'updated_at',
        'id',
        'group_id',
        'name',
        'start_date',
        'end_date',
        'link_allowed',
        'payment_schedule_state',
        'budget_shared',
        'discount_amount',
        'discount_cutoff_amount',
        'discount_cutoff_date',
        'discount_enabled',
    ])
    with Session(engine) as session:
        records = session.query(Seasons).all()
        for col in records:
            outcsv.writerow([
                col.created_at,
                col.updated_at,
                col.id,
                col.team_id,
                col.name,
                col.start_date,
                col.end_date,
                col.link_allowed,
                col.payment_schedule_state,
                col.budget_shared,
                col.discount_amount,
                col.discount_cutoff_amount,
                col.discount_cutoff_date,
                col.discount_enabled
            ])
    outfile.close()

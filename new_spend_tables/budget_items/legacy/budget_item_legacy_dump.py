import csv
from budget_item_class_legacy import BudgetItem
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine

session_pool = sessionmaker(engine)

with open('new_spend_tables/budget_items/budget_items_data_dump.csv', 'w', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'description',
        'target_amount',
        'season_id',
        'category_id',
        'created_at',
        'updated_at',
    ])
    with Session(engine) as session:
        records = session.query(BudgetItem).all()
        for col in records:
            outcsv.writerow([
                col.id,
                col.description,
                col.target_amount,
                col.season_id,
                col.category_id,
                col.created_at,
                col.updated_at,
            ])
    outfile.close()

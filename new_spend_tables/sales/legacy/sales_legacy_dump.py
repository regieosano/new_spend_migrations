import csv
from sales_class_legacy import Sales
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine

session_pool = sessionmaker(engine)

with open('new_spend_tables/sales/sales_test_data_dump.csv', 'w', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'name',
        'created_at',
        'updated_at',

    ])
    with Session(engine) as session:
        records = session.query(Sales).all()
        print(records)
        for col in records:
            outcsv.writerow([
                col.id,
                col.name,
                col.created_at,
                col.updated_at,
            ])

    outfile.close()

import csv
from category_class_legacy import Category
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine

session_pool = sessionmaker(engine)

with open('categories/category_test_data_dump.csv', 'w', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'name',
        'type',
        'is_default',
        'is_hidden',
        'created_at',
        'updated_at',
        'organization_id',


    ])
    with Session(engine) as session:
        records = session.query(Category).all()
        for col in records:
            if col.updated_at is None:
                updated_at = '2021-10-14 15:42:00.079246'
            else:
                updated_at = col.updated_at
            outcsv.writerow([
                col.id,
                col.name,
                None,
                False,
                col.hidden,
                col.created_at,
                updated_at,
                'spdorg_cliayn82a00bb6ot9786n562a',
            ])

    outfile.close()

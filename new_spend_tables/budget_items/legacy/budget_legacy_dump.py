import csv
from zipfile import ZipFile
from budget_class_legacy import Budget
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

with open('new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv', 'w+', encoding='UTF-8', newline='') as outfile:
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow([
        'id',
        'description',
        'target_date',
        'target_amount',
        'payment_method_id',
        'season_id',
        'category_id',
        'created_at',
        'updated_at',
    ])
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(Budget).all()
        for col in records:
            id = 'spdbud_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.description,
                col.target_date,
                col.target_amount,
                col.payment_method_id,
                col.season_id,
                col.category_id,
                col.created_at,
                col.updated_at,
            ])
        with open('new_spend_tables/budget_items/idlookup/budget_items_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)
    outfile.close()

with ZipFile('new_spend_tables/budget_items/zipped/budget_csv_json.zip', 'w') as zipObj:
    zipObj.write(
        'new_spend_tables/budget_items/legacy/dump/budget_data_dump.csv')
    zipObj.write(
        'new_spend_tables/budget_items/idlookup/budget_items_id_lookup.json')
    zipObj.close()

import csv
from budget_item_class_legacy import BudgetItem
from sqlalchemy.orm import Session, sessionmaker
from _database.engine_db_legacy import engine
from cuid import cuid
import json

session_pool = sessionmaker(engine)

category_id_lookup_file = open(
    'new_spend_tables/categories/categories_id_lookup.json')
season_id_lookup_file = open('new_spend_tables/seasons/seasons_id_lookup.json')
category_id_lookup = json.load(category_id_lookup_file)
season_id_lookup = json.load(season_id_lookup_file)

with open('new_spend_tables/budget_items/budget_items_data_dump.csv', 'w+', newline='') as outfile:
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
    id_lookup = {}
    with Session(engine) as session:
        records = session.query(BudgetItem).all()
        for col in records:
            season_id = None
            try:
                season_id = season_id_lookup["%i" % col.season_id]
            except:
                pass
            category_id = None
            try:
                category_id = category_id_lookup["%i" % col.category_id]
            except:
                pass
            id = 'spdbud_%s' % cuid()
            id_lookup[col.id] = id
            outcsv.writerow([
                id,
                col.description,
                col.target_amount,
                season_id,
                category_id,
                col.created_at,
                col.updated_at,
            ])
        with open('new_spend_tables/budget_items/budget_items_id_lookup.json', 'w+') as id_lookup_file:
            json.dump(id_lookup, id_lookup_file)

    outfile.close()

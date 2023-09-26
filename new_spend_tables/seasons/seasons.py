import csv
from sqlalchemy.orm import Session, sessionmaker
from seasons_class import Seasons
from _database.engine_db import engine
import json


source_csv_file = "new_spend_tables/seasons/legacy/dump/season_data_dump.csv"

session_pool = sessionmaker(engine)

group_id_lookup_file = open(
    'new_spend_tables/groups/idlookup/groups_id_lookup.json')
group_id_lookup = json.load(group_id_lookup_file)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_link_enabled_value = True if row['link_allowed'] == 'TRUE' else False
        is_budget_shared_value = True if row['budget_shared'] == 'TRUE' else False
        group_id_value = 'spdgrp_clmudiyk600000cnyx54f5dz5' if row[
            'group_id'] == '' else group_id_lookup[row['group_id']]
        season = Seasons(
            id=row['id'],
            start_date_at=row['start_date'],
            end_date_at=row['end_date'],
            name=row['name'],
            is_link_enabled=is_link_enabled_value,
            is_budget_shared=is_budget_shared_value,
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            group_id=group_id_value,
        )

        with Session(engine) as session:
            session.add(season)
            session.commit()

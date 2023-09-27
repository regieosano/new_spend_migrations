import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from seasons_class import Seasons
from _database.engine_db import engine
import json

source_csv_file = "new_spend_tables/seasons/legacy/dump/season_data_dump.csv"

session_pool = sessionmaker(engine)

season_data = pd.read_csv(source_csv_file)

DUMMY_VALID_GROUP_ID = 'spdgrp_cln1e142f0000tgny36ku23mq'
LENGTH_OF_SEASON_DATA = len(season_data)

# Initialize look-up tables
group_id_lookup_file = open(
    'new_spend_tables/groups/idlookup/groups_id_lookup.json')
group_id_lookup = json.load(group_id_lookup_file)

record = season_data.to_dict()

for i in range(LENGTH_OF_SEASON_DATA):
    is_link_enabled_value = True if record['link_allowed'][i] == 'TRUE' else False
    is_budget_shared_value = True if record['budget_shared'][i] == 'TRUE' else False
    if pd.isna(record['team_id'][i]):
        group_id_value = DUMMY_VALID_GROUP_ID
    else:
        group_id_value = group_id_lookup[record['team_id'][i]]
    season = Seasons(
        id=record['id'][i],
        start_date_at=record['start_date'][i],
        end_date_at=record['end_date'][i],
        name=record['name'][i],
        is_link_enabled=is_link_enabled_value,
        is_budget_shared=is_budget_shared_value,
        created_at=record['created_at'][i],
        updated_at=record['updated_at'][i],
        group_id=group_id_value,
    )

    with Session(engine) as session:
        session.add(season)
        session.commit()

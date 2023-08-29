import csv

from sqlalchemy.orm import Session, sessionmaker
from seasons_class import Seasons
from _database.engine_db import engine


source_csv_file = "seasons/season_test_data_dump.csv"


session_pool = sessionmaker(engine)

with open(source_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_link_enabled_value = True if row['is_link_enabled'] == 'TRUE' else False
        is_budget_shared_value = True if row['is_budget_shared'] == 'TRUE' else False
        season = Seasons(
            id=row['id'],
            start_date_at=row['start_date_at'],
            end_date_at=row['end_date_at'],
            name=row['name'],
            is_link_enabled=is_link_enabled_value,
            is_budget_shared=is_budget_shared_value,
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            group_id=row['group_id'],
        )

        with Session(engine) as session:
            session.add(season)
            session.commit()
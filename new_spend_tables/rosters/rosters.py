import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from rosters_class import Rosters
from _database.engine_db import engine

source_csv_file = "new_spend_tables/rosters/legacy/dump/player_data_dump.csv"

session_pool = sessionmaker(engine)

roster_data = pd.read_csv(source_csv_file)

LENGTH_OF_ROSTER_DATA = len(roster_data)

record = roster_data.to_dict()

for i in range(LENGTH_OF_ROSTER_DATA):
    roster = Rosters(
        id=record['player_id'][i],
        name=record['player_name'][i],
        email='',
    )

    with Session(engine) as session:
        session.add(roster)
        session.commit()

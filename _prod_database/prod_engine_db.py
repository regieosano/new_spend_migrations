from environs import Env
from sqlalchemy import create_engine, URL

env = Env()
env.read_env(".env")

url = URL.create(
    drivername=env.str("SERVER_DRIVERNAME"),
    username=env.str("NEW_SPEND_PROD1_USER"),
    password=env.str("NEW_SPEND_PROD1_PASSWORD"),
    host=env.str("NEW_SPEND_PROD1_HOST"),
    port=env.int("NEW_SPEND_PROD1_PORT"),
    database=env.str("NEW_SPEND_PROD1_DATABASE"),
)

prod_engine = create_engine(url, echo=True)

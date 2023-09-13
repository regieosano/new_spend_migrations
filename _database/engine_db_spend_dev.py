from environs import Env
from sqlalchemy import create_engine, URL

env = Env()
env.read_env(".env")

url = URL.create(
    drivername=env.str("SERVER_DRIVERNAME"),
    username=env.str("SPEND_DEV_USER"),
    password=env.str("SPEND_DEV_PASSWORD"),
    host=env.str("SPEND_DEV_HOST"),
    port=env.int("SPEND_DEV_PORT"),
    database=env.str("SPEND_DEV_DATABASE"),
)

engine = create_engine(url, echo=True)

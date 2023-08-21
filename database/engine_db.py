from environs import Env
from sqlalchemy import create_engine, URL

env = Env()
env.read_env(".env")

url = URL.create(
    drivername=env.str("SERVER_DRIVERNAME"),
    username=env.str("H_IAM_USER"),
    password=env.str("H_IAM_PASSWORD"),
    host=env.str("H_PERSONAL_HOST"),
    port=env.int("H_PORT"),
    database=env.str("H_TEST_DATABASE"),
)

engine = create_engine(url, echo=True)

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


class DbSessionManager:
    USER = "postgres"
    PASSWORD = "1q2w3E4R"
    IP_ADDR = "127.0.0.1"
    DB_NAME = "fast_api_db"

    @staticmethod
    def create_engine():
        engine = \
            create_engine(f"postgresql+psycopg2://{DbSessionManager.USER}:{DbSessionManager.PASSWORD}@"
                          f"{DbSessionManager.IP_ADDR}/{DbSessionManager.DB_NAME}")
        return engine

    @staticmethod
    def create_db():
        engine = DbSessionManager.create_engine()
        if not database_exists(engine.url):
            create_database(engine.url)

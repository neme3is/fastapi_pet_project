from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


class DbSessionManager:
    USER = "postgres"
    PASSWORD = "1q2w3E4R"
    IP_ADDR = "127.0.0.1"
    DB_NAME = "fast_api_db"
    connection = None

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
        return engine

    @staticmethod
    def connect_db():
        engine = DbSessionManager.create_db()
        if DbSessionManager.connection is None:
            db_session = sessionmaker()
            db_session.configure(bind=engine)
            DbSessionManager.connection = db_session()


    @staticmethod
    def add_entity(entity):
        DbSessionManager.connect_db()
        DbSessionManager.connection.add(entity)
        DbSessionManager.connection.commit()

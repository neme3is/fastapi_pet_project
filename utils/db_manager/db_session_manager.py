from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


class DbSessionManager:
    USER = "postgres"
    PASSWORD = "1q2w3E4R"
    IP_ADDR = "127.0.0.1"
    DB_NAME = "fast_api_db"
    session = None

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
        if DbSessionManager.session is None:
            db_session = sessionmaker()
            db_session.configure(bind=engine)
            DbSessionManager.session = db_session()

    @staticmethod
    def add_entity(entity):
        DbSessionManager.connect_db()
        DbSessionManager.session.add(entity)
        DbSessionManager.session.commit()

    @staticmethod
    def query(table):
        return DbSessionManager.session.query(table)

    """
    filtered_query = session.query(users_table).filter(users_table.c.id == 1)
    updated_rows = filtered_query.update({users_table.c.age: 30})
    """
    @staticmethod
    def update(filtered_query, column, value):
        updated_rows = filtered_query.update({column: value})
        DbSessionManager.session.commit()
        return updated_rows


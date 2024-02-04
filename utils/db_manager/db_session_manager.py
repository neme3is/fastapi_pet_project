from sqlalchemy import create_engine


class DbSessionManager:
    USER = "postgres"
    PASSWORD = "1q2w3E4R"
    IP_ADDR = "127.0.0.1"
    DB_NAME = "fast_api_db"

    @staticmethod
    def create_session_obj():
        engine = \
            create_engine(f"postgresql+psycopg2://{DbSessionManager.USER}:{DbSessionManager.PASSWORD}@"
                          f"{DbSessionManager.IP_ADDR}/{DbSessionManager.DB_NAME}")
        engine.connect()


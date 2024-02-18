import sqlalchemy
from sqlalchemy import Integer, String

from utils.db_manager.db_session_manager import DbSessionManager
from utils.orm_models.base_class_orm import Base


class User(Base):

    __tablename__ = 'Users'

    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(String)
    password = sqlalchemy.Column(String)

    @staticmethod
    def add_user(user_name: str, password: str):
        DbSessionManager.add_entity(User(name=user_name, password=password))

    # todo move to common
    @staticmethod
    def get_user_by_name(user_name: str):
        DbSessionManager.connect_db()
        result = DbSessionManager.connection.query(User).filter(User.name == user_name).all()
        return result

from utils.db_manager.db_session_manager import DbSessionManager
from utils.orm_models.base_class_orm import Base

# import orm to initialize tables inside Base

from utils.orm_models.good_model import Good
from utils.orm_models.user_model import User

DbSessionManager.create_db()


engine = DbSessionManager.create_engine()
Base.metadata.create_all(engine, checkfirst=True)

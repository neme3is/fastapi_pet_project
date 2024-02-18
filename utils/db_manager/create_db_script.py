from utils.db_manager.db_session_manager import DbSessionManager
from utils.orm_models.base_class_orm import Base


DbSessionManager.create_db()


engine = DbSessionManager.create_engine()
Base.metadata.create_all(engine, checkfirst=True)

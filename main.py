from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from utils.api_models.user import User
from utils.orm_models.user_model import User as UserOrmModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test-1")
async def test_1():
    return {"message": "Test page 1"}


@app.get("/test-2")
async def test_2():
    return {"message": "Test page 2"}


@app.post("/add-user/")
async def add_user(user: User):
    if len(UserOrmModel.get_user_by_name(user.name)) > 0:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content=user.name)
    UserOrmModel.add_user(user.name, user.password)
    user_id = UserOrmModel.get_user_by_name(user.name)[0].id
    return f"User: {user.name} added, id: {user_id}"

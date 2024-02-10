
from fastapi import FastAPI

from utils.orm_models.user_model import User

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


@app.post("/add-user/{user_name}")
async def add_user(user_name):
    User.add_user(user_name)
    user_id = User.get_user_by_name(user_name)[0].id
    return f"User: {user_name} added, id: {user_id}"


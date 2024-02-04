from fastapi import FastAPI

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

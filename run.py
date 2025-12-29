from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src import UserRepo, UsersModel

app = FastAPI()

@app.get("/")
def greeting():
    return JSONResponse(status_code=200, content={"message": "Hello World"})


@app.post("/insert")
def insert(request: Request, name: str):
    userRepo = UserRepo()
    userRepo.insert_user(name)
    return JSONResponse(status_code=201, content={"message": "User added successfully"})
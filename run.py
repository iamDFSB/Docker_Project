from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src import UserRepo

app = FastAPI()

@app.get("/")
def greeting():
    return JSONResponse(status_code=200, content={"message": "Hello World"})


@app.post("/insert")
def insert(request: Request):
    userRepo = UserRepo()
    body = request.json
    userRepo.insert_user(body["name"])
    return JSONResponse(status_code=201, content={"message": "User added successfully"})
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi_throttle.limiter import RateLimiter
from src import UserRepo

app = FastAPI()
limiter = RateLimiter(times=3, seconds=60)

@app.get("/")
def greeting():
    return JSONResponse(status_code=200, content={"message": "Hello World"})

@app.post("/insert")
def insert(request: Request, name: str):
    userRepo = UserRepo()
    userRepo.insert_user(name)
    return JSONResponse(status_code=201, content={"message": "User added successfully"})


@app.get("/users", dependencies=[Depends(limiter)])
def users():
    userRepo = UserRepo()
    users = userRepo.get_users()
    users_formatted = [
        {"id": user.id, "name": user.name}
        for user in users
    ]
    return JSONResponse(status_code=200, content={"users": users_formatted})
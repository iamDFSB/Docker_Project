from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def greeting():
    return JSONResponse(status_code=200, content={"message": "Hello World"})
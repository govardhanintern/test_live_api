from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/user")
def read_root1():
    return {"message": "Hello, FastAPIabc!"}
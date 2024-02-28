from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.post("/echo/")
def echo(message: str):
    return {"content": message}

@app.get("/hoge/")
def hoge():
    with open("./hoge.txt") as f:
        content = f.read()
    return {"content": content}
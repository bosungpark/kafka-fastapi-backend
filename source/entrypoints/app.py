from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def some_api():
    return {"Hello": "World"}

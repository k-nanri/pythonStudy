from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
def call_api():
    time.sleep(10)
    response = {"message": "success"}
    return response


# 下記で起動
# uvicorn app:app

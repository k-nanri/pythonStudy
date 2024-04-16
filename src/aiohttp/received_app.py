from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def get_request():

    print("Received Request!!")
    response = requests.get("http://127.0.0.1:8000")
    print(response.status_code)
    return {"res": response.json()}


# uvicorn received_app:app --port 8081

import httpx
import logging
import asyncio

logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)


def get_request():

    r = httpx.get("http://localhost:8000/item")
    if r.status_code == 200:
        print("Operate Request Success")
        r_json = r.json()
        print(f"Receive body: {r_json}")


def get_request_log():

    client = httpx.Client(
        event_hooks={
            "request": [log_request],
            "response": [log_response, log_response2, log_response3],
        }
    )
    r = client.get("http://localhost:8000/item")
    if r.status_code == 200:
        print("Operate Request Success")
        r_json = r.json()
        print(f"Receive body: {r_json}")


def post_request():
    body = {"mode": "post", "data": "aaa"}
    r = httpx.post("http://localhost:8000/item", json=body)
    print(r)
    if r.status_code == 200:
        print("Post Request Success")
        print(f"Response body: {r.json()}")


def post_request_exception():
    body = {"mode": "post", "data": "aaa"}
    r = httpx.post("http://localhost:8000/item2", json=body)
    print(r)
    try:
        r.raise_for_status()
        print("Post Request Success")
        print(f"Response body: {r.json()}")
    except httpx.HTTPStatusError as ex:
        print(f"Error Response Status Code: {ex.response.status_code}")


def get_request_except():

    r = httpx.get("http://localhost:8000/item2")
    try:
        r.raise_for_status()
        print("Operate Request Success")
        r_json = r.json()
        print(f"Receive body: {r_json}")
    except httpx.HTTPStatusError as ex:
        print(f"Error Response Status Code: {ex.response.status_code}")


def log_request(request):
    print(f"Request Event Hook request={request}")


def log_response(response):
    print(f"Response Event Hook response={response}")


def log_response2(response):
    print(f"Status Code Check {response.status_code}")


def log_response3(response):
    print("last event hook function")


async def async_get_request():

    async with httpx.AsyncClient() as client:
        r = await client.get("http://localhost:8000/item")

        if r.status_code == 200:
            print(f"Recevice body: {r.json()}")


async def async_post_request():

    async with httpx.AsyncClient() as client:
        body = {"mode": "async", "key": "hogehoge"}
        r = await client.post("http://localhost:8000/item", json=body)
        if r.status_code == 200:
            print(f"Recevice body: {r.json()}")


async def reqeust():

    # task1 = asyncio.create_task(async_get_request())
    task1 = asyncio.create_task(async_post_request())
    await task1


def main():
    # get_request()
    # post_request()
    # asyncio.run(reqeust())
    # get_request_except()
    # post_request_exception()
    get_request_log()


if __name__ == "__main__":
    main()

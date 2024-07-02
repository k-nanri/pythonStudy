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


def post_request():
    body = {"mode": "post", "data": "aaa"}
    r = httpx.post("http://localhost:8000/item", json=body)
    print(r)
    if r.status_code == 200:
        print("Post Request Success")
        print(f"Response body: {r.json()}")


def get_request_except():

    r = httpx.get("http://localhost:8000/item2")
    try:
        r.raise_for_status()
        print("Operate Request Success")
        r_json = r.json()
        print(f"Receive body: {r_json}")
    except httpx.HTTPStatusError as ex:
        print(f"Error Response Status Code: {ex.response.status_code}")


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
    get_request_except()


if __name__ == "__main__":
    main()

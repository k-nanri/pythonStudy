import httpx
import logging

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


def main():
    # get_request()
    post_request()


if __name__ == "__main__":
    main()

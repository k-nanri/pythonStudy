import requests
import backoff
import time

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_tries=5,
                      jitter=None)
def handler():

    print("Start handler")
    try:
        start = time.time()
        response = requests.get("http://localhost:8000", timeout=(5.0, 5.0))
    except Exception as e:
        end = time.time()
        print("occur Exception")
        print("Execute time = " + str(end - start))
        print(e)

        raise e
    
    end = time.time()
    print("End handler time = " + str(end - start))

if __name__ == '__main__':
    handler()
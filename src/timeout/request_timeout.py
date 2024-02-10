"""
下記のコマンドでインストール
pip install timeout-decorator
"""
import time
import timeout_decorator
import requests

@timeout_decorator.timeout(10)
def call_func():

    print("Send Request!!")
    response = requests.get("http://localhost:8000"params=None)
    print("Receive Response!!")

# RESTで長時間応答がないばいのために使用する

if __name__ == '__main__':
    i = 0
    while i < 3:
        call_func()
        i += 1

# RESTを投げるときはどうなる？
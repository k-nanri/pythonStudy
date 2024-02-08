"""
下記のコマンドでインストール
pip install timeout-decorator
"""
import time
import timeout_decorator
import requests

class NewError(Exception):
    pass

# 5秒後にタイムアウトする
# timeout_excaptionでExceptionを指定できる
@timeout_decorator.timeout(5)
@timeout_decorator.timeout(5, timeout_exception=NewError)
def call_func():
    print("Start call_func")
    time.sleep(10)
    print("End call_func")

# RESTで長時間応答がないばいのために使用する

if __name__ == '__main__':
    i = 0
    while i < 3:
        call_func()
        i += 1

# RESTを投げるときはどうなる？
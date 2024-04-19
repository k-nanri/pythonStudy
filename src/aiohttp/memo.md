# aiohttpを使ってみる

## aiohttpとは

非同期で動作するHTTPクライアント／サーバー。
asyncioを使って動作する。
HTTPリクエストのモジュールでは、`requests`がメジャーだと思う。
自分も仕事では`requests`ばかり使っている。

## なぜ、非同期が必要なのか？

リクエストの応答待ちをしている間に他の処理を動かして、効率よく処理をしたいから。
リクエストの応答がなかなか返ってこない間、他の処理は止まってしまう。その間にリクエストを受信してしまうと
サーバー側は処理しきれなくなってしまう。
そのため、リクエストの応答を待っている間にリクエストの受信して他のリクエストを処理できるようにするために
非同期での実行が必要になる。

## aiohttpのインストール

aiohttpモジュールをインストールするだけ。

```python
pip install aiohttp
```

## ハローワールド

GETリクエストのハローワールド。aiohttpのページに書かれているの`await`を使うように
少し変更。

```python
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        resp = await session.get("http://httpbin.org/get")
        print(resp.status)
        print(await resp.text())


asyncio.run(main())
```

## 同期と非同期で処理した場合の実験

リクエストを送信した際に、受信側が別のマイクロサービスに同期でリクエストを送信するケースを実験する。

task1を受信した順番に処理が行われる。

```text
# 送信元
2024-04-20 07:59:04,569 - --- task1 -----
2024-04-20 07:59:04,569 - --- task1 Send!!
2024-04-20 07:59:04,570 - --- task2 -----
2024-04-20 07:59:04,570 - --- task2 Send!!
2024-04-20 07:59:14,606 - --- task1 status = 200
2024-04-20 07:59:14,606 - --- task1{"res":{"message":"success"}}
2024-04-20 07:59:24,612 - --- task2 status = 200
2024-04-20 07:59:24,612 - --- task2{"res":{"message":"success"}}

# 受信側
2024-04-20 07:59:04,572 - Received task1 Request!!
2024-04-20 07:59:14,604 - Send task1 response
INFO:     127.0.0.1:52673 - "GET /task1 HTTP/1.1" 200 OK
2024-04-20 07:59:14,606 - Received task2 Request!!
2024-04-20 07:59:24,611 - Send task2 response
INFO:     127.0.0.1:52674 - "GET /task2 HTTP/1.1" 200 OK
```

### aiohttpのみ

```text
# 送信元
2024-04-20 08:01:19,726 - --- task1 -----
2024-04-20 08:01:19,726 - --- task1 Send!!
2024-04-20 08:01:19,726 - --- task2 -----
2024-04-20 08:01:19,726 - --- task2 Send!!
2024-04-20 08:01:29,740 - --- task1 status = 200
2024-04-20 08:01:29,740 - --- task1{"res":{"message":"success"}}
2024-04-20 08:01:29,740 - --- task2 status = 200
2024-04-20 08:01:29,740 - --- task2{"res":{"message":"success"}}

# 受信側
2024-04-20 08:01:19,728 - Received task1 Request!!
2024-04-20 08:01:19,732 - Received task2 Request!!
2024-04-20 08:01:29,738 - Send task1 response
INFO:     127.0.0.1:53064 - "GET /task1 HTTP/1.1" 200 OK
2024-04-20 08:01:29,739 - Send task2 response
INFO:     127.0.0.1:53065 - "GET /task2 HTTP/1.1" 200 OK
```

### requestsとaiohttpの混在

## 性能を測ってみるとどうなる？


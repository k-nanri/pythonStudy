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

### aiohttpのみ

### requestsとaiohttpの混在

## 性能を測ってみるとどうなる？


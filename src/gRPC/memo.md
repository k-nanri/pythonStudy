# grpcとは

https://knowledge.sakura.ad.jp/24059/

RESTの場合、テキストベースで情報をやり取りするため、データの転送効率が悪い。また、バイナリデータを扱いにく。
gRPCは、テキストベースのJSONの代わりにProtobufというフォーマットを用いて、データの転送効率を高速化しており、バイナリデータのやり取りも可能にしている。
データは圧縮されたフォーマットであるため、JSONのように人間が読みやすい形にはなっていない。

外部ユーザが理解しやすい公開APIやシンプルなデータ通信をする場合はRESTがよい。
リアルタイム通信が必要な場合や双方向ストリーミング、リアルタイムでメッセージの送受信が可能なので、
高速な通信やリアルタイムのストリーミング、大量のデータログを必要とする内部システムに適している。

https://tech-lab.sios.jp/archives/38015

# Setup

gRPCに必要なモジュールをインストールする

```python
pip install grpcio
pip install grpcio-tools
```

## フォルダ構成

作業前フォルダ構成

```shell
.
|-- proto
|     +- user.proto
|-- users.json

```

## プロトコル定義ファイルからコードを生成

protocモジュールを使って、プロトコル定義からソースを生成

```python
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/user.proto
```

## サーバー/クライアントの実装

サーバー側では、<サービス名>Servicerというクラスを継承したクラスを実装する。
継承するクラスは、user_bp2_grp.pyで実装されている。
あとは、サイト通りに実装すればよい。

## ストリーミング

1リクエストに対して、1レスポンスを返すのではなく、接続上で複数個のデータを送る通信方式。
gRPCのストリーミング通信には、3つのタイプがある。

- Server streaming RPC (単方向サーバーストリーミング)
- Client streaming RPC (単方向クライアントストリーミング)
- Bidirectional streaming RPC (双方向ストリーミング)

https://zenn.dev/hsaki/books/golang-grpc-starting/viewer/stream

# クライアントからサーバーが複数応答

サーバー側は応答結果をyieldで返す必要がある。
クライアント側は関数の戻り値をイテレーティブとして処理する。
```python
for response in stub.sayHello(
    hellostreamingworld_pb2.HelloRequest(name="you")
):
    print("Greeter client received from async generator: " + response.message)
```

非同期の場合は、read関数で待ち合わせして、取得結果がEOFでなければ処理する。

```python
hello_stream = stub.sayHello(hellostreamingworld_pb2.HelloRequest(name="you"))
while True:
    response = await hello_stream.read()
    if response == grpc.aio.EOF:
        break
    print("Greeter client received from direct read: " + response.message)

```


# クライアントから複数送って、サーバは一個だけ返す

## 参考

https://knowledge.sakura.ad.jp/24059/
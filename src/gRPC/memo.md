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

## プロトコル定義ファイルからコードを生成

protocモジュールを使って、プロトコル定義からソースを生成

```python
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/user.proto
```

## サーバー/クライアントの実装

サーバー側では、<サービス名>Servicerというクラスを継承したクラスを実装する。
継承するクラス、`grpc_tools.protoc`コマンドで生成したソースコードで実装されている。
ここでは、user_bp2_grp.pyがそれにあたる。

## ストリーミング

1リクエストに対して、1レスポンスを返すのではなく、接続上で複数個のデータを送る通信方式。
gRPCのストリーミング通信には、3つのタイプがある。

- Server streaming RPC (単方向サーバーストリーミング)
- Client streaming RPC (単方向クライアントストリーミング)
- Bidirectional streaming RPC (双方向ストリーミング)

https://zenn.dev/hsaki/books/golang-grpc-starting/viewer/stream

## クライアントからサーバーが複数応答（単方向サーバーストリーミング）

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


## クライアントから複数送って、サーバは一個だけ返す（単方向クライアントストリーミング）

クライアントからリクエストを分割して送り、サーバー側は全てのリクエストを受けてレスポンスを返す。
大きなデータを分割してアップロードしたい場合などに使える。

https://sqripts.com/2023/03/02/36920/

### サーバー側の実装

サーバー側は関数のパラメータにIterableのデータを持つ。
このIterableに複数のリクエストが入っている

```python
def get_client_stream(self, request_iter: Iterable[user_pb2.UserRequest], context):
```

Iterable型のパラメータがクライアントからのリクエストになる。このパラメータをループでリクエストを処理して、最後にクライアントに返す実装になる。

```python
for request in request_iter:
    user_id = request.id
    if str(user_id) in users:
        print("user count up")
        user_cnt += 1

result = user_pb2.User()
result.id = user_cnt
return user_pb2.UserResponse(error=False, user=result)
```

### クライアント側の実装

クライアント側は、サーバ側に渡すデータ用の関数を作成してyieldで1つずつサーバ側に
渡す。

```python
def create_data():
    for user_id in [1, 2, 3]:
        print("user_id = " + str(user_id))
        req = user_pb2.UserRequest(id=user_id)
        yield req


def client_streaming():
    print("call client streaming!!")
    with grpc.insecure_channel("localhost:1234") as channel:
        stub = user_pb2_grpc.UserManagerStub(channel)
        response = stub.get_client_stream(create_data())
        pprint.pprint(response)
```

## 双方向での通信（双方向ストリーミング）

サーバー／クライアントが任意のタイミングでリクエストやレスポンスを送る送ることができる。
チャットのやり取りをイメージしてもらえるといいかと思う。

### サーバー側の実装

クライアント側のリクエストは、Iterable型なので、for文でリクエストを処理する。
サーバー側の複数の応答は、yieldを使って１つずつ返している。

```python
for message in request_itr:
    print(
        "Receive new message!! [id: {}, msg: {}]".format(
            message.id, message.message
        )
    )

    reply_messages = []
    reply_messages.append(
        user_pb2.ChatMessage(id=message.id, message="Thank!!!")
    )
    reply_messages.append(
        user_pb2.ChatMessage(id=message.id, message="good day!!!")
    )

    for message in reply_messages:
        yield message
```

### クライアント側の実装

サーバー側の関数をコールして、戻り値はIterable側なのでfor文でレスポンスを処理する。


```python
def send_message(stub, msg, id):
    messages = []
    messages.append(user_pb2.ChatMessage(id=id, message=msg))
    responses = stub.connect_chat(iter(messages))
    for res in responses:
        print("Received message [id={}, msg={}]".format(res.id, res.message))


def client_streaming():
    id = 1
    with grpc.insecure_channel("localhost:1234") as channel:
        stub = user_pb2_grpc.UserManagerStub(channel)
        print("--- Input your message -------")
        while True:
            msg = input("Input message >")
            send_message(stub, msg, id)
            id += 1
```

##　最後に

簡単なハローワールドレベルでgRPCを使ってみた。
メッセージの型も明確に定義して利用しなければならないため、設計時に通信相手との意識合わせが必須。RESTに関しても同様だが、gRPCの方が厳格だ。
より高速な処理が求めまれるときはgRPCの方が良さそう。
監視系に関しても次世代ネットワークの監視は、gRPCとかを使うことになるように感じているので、kafkaもちゃんと理解しないといけないなと感じた。


## 参考

yieldの使い方

https://knowledge.sakura.ad.jp/24059/
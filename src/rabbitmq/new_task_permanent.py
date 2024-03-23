import pika
import sys

# RabbitMQに接続
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# キューを作成
channel.queue_declare(queue="hello", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World"
channel.basic_publish(exchange="", routing_key="hello", body=message)
print("  [x] Send " + message)

# コネクションのクローズ
connection.close()

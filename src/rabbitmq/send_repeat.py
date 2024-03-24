import pika
import sys
import time

# RabbitMQに接続
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# キューを作成
channel.queue_declare(queue="hello", durable=True)


for i in range(50):
    message = "Message No." + str(i)
    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print("  [x] Send " + message)
    time.sleep(0.5)

# コネクションのクローズ
connection.close()

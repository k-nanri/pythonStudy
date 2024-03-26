import pika
import time

# RabbitMQに接続
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#
channel.exchange_declare(exchange="logs", exchange_type="fanout")

for i in range(50):
    message = "Message No." + str(i)
    channel.basic_publish(
        exchange="logs",
        routing_key="",
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print("  [x] Send " + message)
    time.sleep(0.5)

# コネクションのクローズ
connection.close()

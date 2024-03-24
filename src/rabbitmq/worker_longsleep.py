import sys
import os
import pika
import time


def callback(channel, method, properties, message):
    print(f"  [x] Received {message.decode()}")
    time.sleep(5)
    print("   [x] Done")
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    # RabbitMQに接続
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    # キューを作成
    channel.queue_declare(queue="hello", passive=True)
    channel.basic_qos(prefetch_count=1)

    print("  [*] Waiting for message. To exit press CTRL+C")
    channel.basic_consume(queue="hello", on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

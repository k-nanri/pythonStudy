import sys
import os
import pika


def callback(channel, method, properties, message):
    print("  [x] Received " + str(message))
    print("      method: " + str(method))
    print("      properties: " + str(properties))


def main():
    # RabbitMQに接続
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    print("  [*] Waiting for message. To exit press CTRL+C")
    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)
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

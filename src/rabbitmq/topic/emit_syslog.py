import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

routing_keys = ["syslog.debug", "syslog2.debug"]

for routing_key in routing_keys:
    message = "topic=" + str(routing_key) + " message!!"
    print("Send message [" + str(message) + "]")
    channel.basic_publish(exchange="topic_logs", routing_key=routing_key, body=message)
    time.sleep(1)

connection.close()

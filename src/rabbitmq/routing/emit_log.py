import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

# severity = sys.argv[1] if len(sys.argv) > 1 else "info"
# message = " ".join(sys.argv[2:]) or "Hello World!"
# channel.basic_publish(exchange="direct_logs", routing_key=severity, body=message)
# print(f" [x] Sent {severity}:{message}")

messages = [
    {"level": "debug", "message": "Debug Message in console"},
    {"level": "info", "message": "Info Message in console"},
    {"level": "warn", "message": "Warn Message in console"},
    {"level": "error", "message": "Error Message in console"},
]

for message in messages:
    channel.basic_publish(
        exchange="direct_logs", routing_key=message["level"], body=message["message"]
    )
    print("Send " + message["message"])
    time.sleep(1)

connection.close()

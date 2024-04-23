import pika
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logger.DEBUG)
handler_format = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(handler_format)
logger.addHandler(handler)

connection = pika.BlockkingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.Channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

binding_keys = ["syslog.debug"]

for binding_key in binding_keys:
    result = channel.queue_declare("", exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(
        exchange="topic_logs", queue_name=queue_name, routing_key=binding_key
    )

logger.info(" [*] Waitting for logs. To exit press CTRL+C")

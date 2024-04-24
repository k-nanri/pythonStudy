import pika
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler_format = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(handler_format)
logger.addHandler(handler)


def callback(ch, method, properties, body):
    logger.debug("=== callback log =========")
    logger.debug(f"{method.routing_key}: {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

binding_keys = ["syslog.debug"]

for binding_key in binding_keys:
    result = channel.queue_declare("", exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key=binding_key)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

logger.info(" [*] Waitting for logs. To exit press CTRL+C")
channel.start_consuming()

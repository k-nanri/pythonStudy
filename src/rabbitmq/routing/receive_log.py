import pika
import sys
import logging

# debug/info はファイルに出力
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("./receive.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s  %(asctime)s  [%(name)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# warn/errorはコンソール
logger2 = logging.getLogger("LogTest")
logger2.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
handler_format = logging.Formatter("%(asctime)s - %(message)s")
stream_handler.setFormatter(handler_format)
logger2.addHandler(stream_handler)

severities = ["debug", "info", "warn", "error"]


def callback_for_debug(ch, method, properties, body):
    print("-- debug callback ----")
    logger.debug(f" [x] {method.routing_key}:{body}")


def callback_for_info(ch, method, properties, body):
    print("-- info callback ----")
    logger.info(f" [x] {method.routing_key}:{body}")


def callback_for_warn(ch, method, properties, body):
    print("-- warn callback ----")
    logger2.warning(f" [x] {method.routing_key}:{body}")


def callback_for_error(ch, method, properties, body):
    print("-- error callback ----")
    logger2.error(f" [x] {method.routing_key}:{body}")


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
# channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
# result = channel.queue_declare(queue="", exclusive=True)
# queue_name = result.method.queue

for severity in severities:

    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue
    # channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=severity)
    channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=severity)

    if severity == "debug":

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback_for_debug, auto_ack=True
        )

    if severity == "info":
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback_for_info, auto_ack=True
        )

    if severity == "warn":
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback_for_warn, auto_ack=True
        )

    if severity == "error":
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback_for_error, auto_ack=True
        )

print(" [*] Waiting for logs. To exit press CTRL+C")


channel.start_consuming()

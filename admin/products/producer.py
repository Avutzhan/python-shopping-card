import pika

params = pika.URLParameters('amqps://mtbcldam:FGxZGanbpBD4ehlQU_-co1kivLAiZtku@snake.rmq2.cloudamqp.com/mtbcldam')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')

import pika

params = pika.URLParameters('amqps://mtbcldam:FGxZGanbpBD4ehlQU_-co1kivLAiZtku@snake.rmq2.cloudamqp.com/mtbcldam')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callBack(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callBack, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

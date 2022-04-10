# import pika
#
# params = pika.URLParameters('amqps://trtpnkbs:AJYD9Xj0JfjRbzhsNtktapH7uW02WtZi@moose.rmq.cloudamqp.com/trtpnkbs')
#
# connection = pika.BlockingConnection(params)
#
# channel = connection.channel()
#
# channel.queue_declare(queue='admin')
#
#
# def callBack(ch, method, properties, body):
#     print('Received in admin')
#     print(body)
#
#
# channel.basic_consume(queue='admin', on_message_callback=callBack, auto_ack=True)
#
# print('Started Consuming')
#
# channel.start_consuming()
#
# channel.close()

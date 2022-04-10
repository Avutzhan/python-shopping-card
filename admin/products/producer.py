import pika, json

params = pika.URLParameters('amqps://trtpnkbs:AJYD9Xj0JfjRbzhsNtktapH7uW02WtZi@moose.rmq.cloudamqp.com/trtpnkbs')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

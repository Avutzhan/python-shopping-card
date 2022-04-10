import pika, json
from app import Product, db

params = pika.URLParameters('amqps://trtpnkbs:AJYD9Xj0JfjRbzhsNtktapH7uW02WtZi@moose.rmq.cloudamqp.com/trtpnkbs')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callBack(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callBack, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

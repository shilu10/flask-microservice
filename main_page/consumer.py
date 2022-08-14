import pika, json
from main import *

#params = pika.URLParameters("amqps://bsphtlrq:n2ashT-9nP1K6s4SUzgeo9e_Fpbx5amz@gull.rmq.cloudamqp.com/bsphtlrq")
params = pika.URLParameters("amqps://localhost")
connection = pika.BlockingConnection(parameters=params)
print(connection, "consumer is running!!!!")
# initialize the channel 
channel = connection.channel()
channel.queue_declare(queue='product')


def consume(channel, event, properties, body):
    data = json.loads(body)
    print(data, event, properties, channel)
    if properties.content_type == 'product-created': 
        product = ProductDisplay(id = data.get("id"), title = data.get("title"), image = data.get("image"), likes = data.get("likes"))
        db.session.add(product)
        db.session.commit()
        db.session.close()

    if properties.content_type == 'product-deleted':
        product = ProductDisplay.query.filter_by(id=data).first()
        db.session.delete(product)
        db.session.commit()
        db.session.close()

    if properties.content_type == "product-updated": 
        print(data.get("id"))
        product = ProductDisplay.query.filter_by(id=data.get("id")).first()
        product.title = data.get("title")
        product.image = data.get("image")
        product.likes = data.get("likes") 
        db.session.commit()
        db.session.close()
 

channel.basic_consume(queue='product', on_message_callback=consume, auto_ack=True)
print("started consuming messages")
channel.start_consuming()
channel.close()

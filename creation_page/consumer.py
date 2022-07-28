import pika, json
import os 
print(os.getcwd())
from main import *

params = pika.URLParameters("amqps://bsphtlrq:n2ashT-9nP1K6s4SUzgeo9e_Fpbx5amz@gull.rmq.cloudamqp.com/bsphtlrq")
connection = pika.BlockingConnection(parameters=params)
print(connection, "consumer is running!!!!")

# initialize the channel 
channel = connection.channel()
channel.queue_declare(queue='likes')

def consume(channel, event, properties, body):
    data = json.loads(body)
    print(data, "-----data------")
    if properties.content_type == 'product-liked': 
        product = Product.query.filter_by(id=data).first()
        product.likes += 1 
        db.session.commit()
        db.session.close()

channel.basic_consume(queue='likes', on_message_callback=consume, auto_ack=True)
print("started consuming messages")
channel.start_consuming()
channel.close()
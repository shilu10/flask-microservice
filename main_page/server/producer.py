import pika, json

def publish(event, body): 
    print("started the producers in main-page microservice!!!")
    properties = pika.BasicProperties(event)
    params = pika.URLParameters("amqps://bsphtlrq:n2ashT-9nP1K6s4SUzgeo9e_Fpbx5amz@gull.rmq.cloudamqp.com/bsphtlrq")

    # connection to the queue
    connection = pika.BlockingConnection(parameters=params)

    # initialize the channel 
    channel = connection.channel()
    print(channel, connection)

    channel.basic_publish(exchange='', routing_key='likes', body=json.dumps(body), properties=properties)
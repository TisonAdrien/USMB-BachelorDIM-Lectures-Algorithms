# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:11:55 2017

@author: tisonad
"""

import pika
import os

# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://ftgfmiyj:i5k7buEpy1v5Xe2HVnKHe7CrYZ0v3veM@lark.rmq.cloudamqp.com/ftgfmiyj'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params) 
# Connect to CloudAMQP

channel = connection.channel()
#Declare the channel
channel.queue_declare(queue='presentation', durable=True)

#Function callback : print the received message
def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)

#Declare the listener
channel.basic_consume(callback,
					queue='presentation',
					no_ack=True)

#Message for waiting
print(" [*] Waiting for messages. To exit press CTRL+C")
#Launch the listener
channel.start_consuming()





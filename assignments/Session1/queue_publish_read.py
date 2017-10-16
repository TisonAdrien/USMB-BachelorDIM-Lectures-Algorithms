# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:31:22 2017

@author: tisonad
"""

import pika
import os
import argparse

#Initialize a parser for choose if we want read or publish
parser = argparse.ArgumentParser(description='-read for read')

#Declare the read argument
parser.add_argument('-read',
					dest='reader',
					action='store_true',
					help='Activate the read mode'
					)
args = parser.parse_args()
#Read is the action todo, True : Read / False : Publish
read = args.reader

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
channel.queue_declare(queue='presentation')

#Declare th number of responses global for update in callback when we read
number_response = 0
def callback(ch, method, properties, body):
	#Increment the number of responses
	global number_response
	number_response = number_response+1
	#Print the received message
	print(" [x] %r - Received %r" % (number_response,body))

if(read):
	#Read messages
	channel.basic_consume(callback,
						queue='presentation',
						no_ack=True)
	print(" [*] Waiting for messages. To exit press CTRL+C")
	channel.start_consuming()
else:
	#Publish a first message
	channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='First message')
	print(" [x] Sent 'First message'")
	#Publish a second message
	channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Second message')
	print(" [x] Sent 'Second message'")
	#publish a third message
	channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Other message')
	print(" [x] Sent 'Other message'")
	#close the connection
	connection.close()

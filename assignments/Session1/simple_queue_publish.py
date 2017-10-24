# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:11:55 2017

@author: tisonad
"""

import pika
import os
import argparse

#Initialize a parser for choose if we want concurrency
parser = argparse.ArgumentParser(description='-concurrency for activate persistent message mode')

#Declare the concurrency argument
parser.add_argument('-concurrency',
					dest='concurrency',
					action='store_true',
					help='Activate the persistent message mode'
					)
args = parser.parse_args()
#Concurrency == True : Persistant message mode activated
persistent = args.concurrency

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
if(persistent):
	#Send a persistent message to th channel
	channel.basic_publish(exchange='',
	                      routing_key='presentation',
	                      body='Hello World!',
						  properties=pika.BasicProperties(
	                         delivery_mode = 2, # make message persistent
	                      ))
else:
	#Send a message to the channel
	channel.basic_publish(exchange='',
	                      routing_key='presentation',
	                      body='Hello World!'
	                      )
#Print message for see if it's work
print(" [x] Sent 'Hello World!'")
#Close the connection
connection.close()
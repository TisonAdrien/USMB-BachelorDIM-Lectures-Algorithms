# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:01:05 2017

@author: tisonad
"""

import pika
import os

# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://ftgfmiyj:i5k7buEpy1v5Xe2HVnKHe7CrYZ0v3veM@lark.rmq.cloudamqp.com/ftgfmiyj'

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

def doSomething(request_params):
    if(request_params == "b'Ping'"):
        rep = 'Pong'
    else:
        rep = 'Fine and you ?'
    print("Request : %r" % request_params)
    print("Response : %r" % rep)
    return rep

def on_request(ch, method, props, body): #process and reply function
        request_param = str(body)# retrieve input parameters
        response = doSomething(request_param) #process the message
        ch.basic_publish(exchange='', #reply
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
correlation_id = props.correlation_id),
                         		body=str(response))
        ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge 

# initiate the connexion and setup the communication channel
connection = pika.BlockingConnection(params) 
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')
# wait for requests
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

channel.start_consuming()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:38:01 2017

@author: tisonad
"""

import pika
import os
import uuid


# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://ftgfmiyj:i5k7buEpy1v5Xe2HVnKHe7CrYZ0v3veM@lark.rmq.cloudamqp.com/ftgfmiyj'

corr_id = str(uuid.uuid4())

def on_response(ch, method, properties, body):
    if (properties.correlation_id == corr_id):
        print(body)
    else:
        raise Exception('l\'id de correlation est différent')

params = pika.URLParameters(amqp_url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()

request_msg = 'Hi ! How fine ?'

result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue


channel.basic_publish(exchange='',
                           routing_key='rpc_queue',
                           properties=pika.BasicProperties(
                                 reply_to = callback_queue,
                                 correlation_id = corr_id,),
                                 body=request_msg)
print('[x] Sent message :)')

# wait for requests
channel.basic_consume(on_response, queue=callback_queue, no_ack=True)

channel.start_consuming()

connection.close()

                           
                    
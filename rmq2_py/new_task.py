#Michael P Murphy
#! /usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

message = ' '.join(sys.argv[1:]) or "I would like to say Hello to the world!"
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2))
print(" [x] Sent %r" % message)

connection.close()
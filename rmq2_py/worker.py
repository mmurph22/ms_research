#Michael P Murphy
#! /usr/bin/env python
import pika
import sys
import os
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        print (" [R] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print (" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', 
            on_message_callback=callback, 
            auto_ack=False)

    print(' [....] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

#*********Runnable
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('GIRL INTERRUPTED!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

def send_rmq_message(filename):
    try:
        credentials = pika.PlainCredentials(os.getenv("RMQ_USER"), os.getenv("RMQ_PASS"))
        parameters = pika.ConnectionParameters(
            host=os.getenv("RMQ_HOST"),
            port=int(os.getenv("RMQ_PORT")),
            virtual_host=os.getenv("RMQ_VHOST"),
            credentials=credentials
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='webcam_images', durable=True)

        message = {"filename": filename, "status": "captured"}
        channel.basic_publish(
            exchange='',
            routing_key='webcam_images',
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print(f"📨 Metadata dikirim ke RMQ: {message}")
        connection.close()

    except Exception as e:
        print(f"❌ RMQ Error: {e}")

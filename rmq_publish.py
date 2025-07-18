import pika
import json
import os
import socket
from dotenv import load_dotenv

load_dotenv()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def send_rmq_message(filename):
    try:
        ip_address = get_local_ip()

        # Hanya ini yang dipakai sebagai message
        message = {
            "filename": filename,
            "status": "captured",
            "ip_address": ip_address
        }

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

        # Gunakan message yang sudah lengkap
        channel.basic_publish(
            exchange='',
            routing_key='webcam_images',
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print(f"Metadata dikirim ke RMQ: {message}")
        connection.close()

    except Exception as e:
        print(f"RMQ Error: {e}")

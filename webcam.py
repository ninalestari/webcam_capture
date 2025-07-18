import cv2
import time
from datetime import datetime
from ftp_upload import upload_to_ftp
from rmq_publish import send_rmq_message

def start_camera_capture():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Tidak bisa ambil gambar dari kamera.")
            break

        filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"✅ Gambar disimpan: {filename}")

        upload_to_ftp(filename)
        send_rmq_message(filename)

        time.sleep(15)
    cap.release()

from flask import Flask
import threading
from webcam import start_camera_capture

app = Flask(__name__)
camera_thread = None

@app.route('/')
def index():
    global camera_thread
    if not camera_thread or not camera_thread.is_alive():
        camera_thread = threading.Thread(target=start_camera_capture, daemon=True)
        camera_thread.start()
    return "📸 Webcam is capturing every 15 seconds..."

if __name__ == '__main__':
    app.run(debug=True)

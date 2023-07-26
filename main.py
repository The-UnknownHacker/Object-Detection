import cv2
import numpy as np
import time
from flask import Flask, Response, render_template_string
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()
phone_detected_sound = pygame.mixer.Sound('BUZZER_2.wav') 

# Load the YOLO model
config_file = "yolov3-tiny.cfg"
weights_file = "yolov3-tiny.weights"

# Check if the configuration file exists in the current directory
if not os.path.exists(config_file):
    raise FileNotFoundError(f"Configuration file '{config_file}' not found in the current directory.")

net = cv2.dnn_DetectionModel(weights_file, config_file)
net.setInputSize(416, 416)
net.setInputScale(1.0/255)
net.setInputSwapRB(True)

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

colors = np.random.uniform(0, 255, size=(len(classes), 3))

app = Flask(__name__)

def detect_objects():
    # Load webcam
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    starting_time = time.time()
    frame_id = 0

    while True:
        # Read webcam
        _, frame = cap.read()
        frame_id += 1
        height, width, channels = frame.shape

        # Detecting objects
        class_ids, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)

        # Visualising data
        phones_detected = 0  # Counter for phones detected in the frame

        if len(class_ids) > 0:
            for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), boxes):
                x, y, w, h = box
                label = str(classes[class_id])
                color = colors[class_id]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, color, 3)

                # Check if the detected object is a cell phone
                if label.lower() == 'cell phone':
                    phones_detected += 1

        elapsed_time = time.time() - starting_time
        fps = frame_id / elapsed_time
        cv2.putText(frame, "FPS: " + str(round(fps, 2)), (40, 670), font, .7, (0, 255, 255), 1)
        cv2.putText(frame, "press [esc] to exit", (40, 690), font, .45, (0, 255, 255), 1)

        # If cell phones are detected, play the sound
        if phones_detected > 0:
            phone_detected_sound.play()

        # Encode frame as JPEG to send via Flask
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_data = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n\r\n')

        key = cv2.waitKey(1)
        if key == 27:
            print("[button pressed] ///// [esc].")
            print("[feedback] ///// Videocapturing successfully stopped")
            break

    cap.release()

@app.route('/')
def index():
    return render_template_string('<img src="{{ url_for(\'video_feed\') }}" />')

@app.route('/video_feed')
def video_feed():
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

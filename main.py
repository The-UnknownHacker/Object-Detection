import cv2
import numpy as np
import time

# Load the YOLO model
config_file = "Real-Time Object Detection OpenCV Python Source Code/configuration/yolov3-tiny.cfg"
weights_file = "Real-Time Object Detection OpenCV Python Source Code/weights/yolov3-tiny.weights"
net = cv2.dnn_DetectionModel(weights_file, config_file)
net.setInputSize(416, 416)
net.setInputScale(1.0/255)
net.setInputSwapRB(True)

classes = []
with open("Real-Time Object Detection OpenCV Python Source Code/configuration/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

colors = np.random.uniform(0, 255, size=(len(classes), 3))

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
    if len(class_ids) > 0:
        for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), boxes):
            x, y, w, h = box
            label = str(classes[class_id])
            color = colors[class_id]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, color, 3)

    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (40, 670), font, .7, (0, 255, 255), 1)
    cv2.putText(frame, "press [esc] to exit", (40, 690), font, .45, (0, 255, 255), 1)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        print("[button pressed] ///// [esc].")
        print("[feedback] ///// Videocapturing successfully stopped")
        break

cap.release()
cv2.destroyAllWindows()

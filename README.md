
## This Project is now deprecated you can still use it and it works amazingly well, But I won't be updating it anymore after August 2023


Real-Time Object Detection using YOLOv3-tiny
This project demonstrates real-time object detection using the YOLOv3-tiny model in OpenCV. 
The YOLO (You Only Look Once) model is an efficient and powerful deep-learning model for object detection.

Dependencies
Before running the project, ensure you have the following dependencies installed:

Also Make sure that you change your path to the valid path of the config file

You can find the path by - Right Clicking on the yolo-tiny.weights - (Or any file dependencies that I have Listd Below) and click copy path - Then Change the slashes from this \ to / and run the code


OpenCV (cv2) library
Numpy library
You can install the required libraries using pip:


``` pip install opencv-python numpy ```

Getting Started
Clone or download this repository to your local machine.

Ensure you have the YOLOv3-tiny configuration file, weights file, and class labels file:

Configuration file: yolov3-tiny.cfg

Weights file: yolov3-tiny.weights

Class labels file: coco.names

Connect your webcam or ensure you have a video source available.

Running the Project
To run the real-time object detection, execute the main.py script:


``` python main.py ```

This script will open the webcam and start detecting objects in real time. Detected objects will be surrounded by bounding boxes, and the corresponding class labels and confidence scores will be displayed.

Press the 'ESC' key to stop the video capture and close the window.

Customizing the Project
If you want to use a different YOLO model or adjust detection parameters, you can modify the main.py script accordingly. For example, you can change the confidence threshold or non-maximum suppression (NMS) threshold to control the number of detected objects.

References
YOLO (You Only Look Once) paper: https://arxiv.org/abs/1506.02640
YOLOv3-tiny configuration and weights: https://github.com/pjreddie/darknet/tree/master/cfg

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and use the code for your own projects!

If you have any questions or issues, please feel free to reach out.

Happy object detection! 🚀

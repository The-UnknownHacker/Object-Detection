# Real-Time Object Detection with YOLOv3-tiny

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project demonstrates **real-time object detection** using the **YOLOv3-tiny** model in OpenCV. YOLO (You Only Look Once) is an efficient and powerful deep-learning model for object detection, designed to process images in real time.

> **Note:** This project is now deprecated. While it still works well, it will no longer be updated after August 2023.

## Dependencies

Before running the project, ensure you have the following dependencies installed:

- **OpenCV (cv2)**
- **Numpy**

You can install these libraries using pip:

```sh
pip install opencv-python numpy
```


Make sure to adjust the paths in your configuration to match the location of your config files. You can do this by:

1. Right-clicking on the `yolov3-tiny.weights` (or any file listed below).
2. Clicking "Copy Path".
3. Changing the slashes from `\` to `/`.

## Getting Started

1. Clone or download this repository to your local machine.
2. Ensure you have the following files:
   - Configuration file: `yolov3-tiny.cfg`
   - Weights file: `yolov3-tiny.weights`
   - Class labels file: `coco.names`
3. Connect your webcam or ensure you have a video source available.

## Running the Project

To run the real-time object detection, execute the `main.py` script:

```sh
python main.py
```


This script will open the webcam and start detecting objects in real time. Detected objects will be surrounded by bounding boxes, and the corresponding class labels and confidence scores will be displayed.

Press the 'ESC' key to stop the video capture and close the window.

## Customizing the Project

If you want to use a different YOLO model or adjust detection parameters, you can modify the `main.py` script accordingly. For example, you can change the confidence threshold or non-maximum suppression (NMS) threshold to control the number of detected objects.

## References

- [YOLO (You Only Look Once) paper](https://arxiv.org/abs/1506.02640)
- [YOLOv3-tiny configuration and weights](https://github.com/pjreddie/darknet/tree/master/cfg)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and use the code for your own projects!

If you have any questions or issues, please feel free to reach out.

Happy object detection! 🚀

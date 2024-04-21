# Red Flag Detection using YOLOv8x

This project aims to detect red flags in images using YOLOv8, a state-of-the-art object detection algorithm. The detection of red flags can have various applications such as safety monitoring, hazard detection, or even in the context of flag recognition.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Acknowledgements](#acknowledgements)

## Introduction

This project utilizes YOLOv8, an advanced object detection algorithm, to detect red flags in images. The model is trained on a dataset containing images with red flags and utilizes transfer learning to fine-tune the pre-trained YOLOv8 model specifically for this task and all the images are annoted using https://roboflow.com/.

## Installation

To run the code and perform red flag detection, you'll need the following dependencies:

Installation

1. Clone the repository:
```bash
https://github.com/Bikas0/Red-Flag-Detection-using-YOLOv8.git
```
2. Create a virtual environment
```bash
python -m venv venv
       or
conda create -n red_flag python=3.10
```
Activate virtual environment
```bash
cd venv
cd Scripts
activate
cd ../..
```
or

```bash
conda activate red_flag
```
or

```bash
cd venv
source bin/activate
cd ..
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download YOLOv8 weights file and place it in the appropriate directory.

## Usage

To perform red flag detection on an image, you can use the provided main.py script. Simply provide the image path (image_path = "image path") and trained model weight path (prediction_model = YOLO("model path here") from the main.py file, and the script will output the detected red flags along with their bounding boxes.


1. Modify the main.py script to specify the path to your image file.

2. Run the script:
```bash
python main.py
```

## Training

If you wish to train the YOLOv8 model on your own dataset for red flag detection, you can follow these steps:

1. *Dataset Preparation*: Gather a dataset containing images with red flags along with corresponding annotations (bounding boxes) using roboflow.
2. *Configuration*: Modify the YOLOv8 configuration file (yolov8.cfg) to suit your dataset and training preferences(use roboflow generated code for access the annoted dataset) .
3. *Training*: Train the model using the provided (Red_Flag_Detection_using_YOLOv8.ipynb) notebook file.
4. *Evaluation*: Evaluate the trained model on a validation set use (Inference red flag.ipynb) notebook file.

## Acknowledgements

This project is built upon the YOLOv8 implementation by Ultralytics LLC. We acknowledge their contribution to the field of object detection and thank them for providing an open-source implementation.






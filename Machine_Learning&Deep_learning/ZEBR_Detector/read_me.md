# Animal Detection

This repository contains a YOLOv8 model trained to detect four animal classes: elephant, zebra, buffalo, and rhino. The model performs real-time detection using a live camera feed.

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
- [Inference](#inference)
- [Usage](#usage)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <github-repo-link>
   cd <github-repo-directory> 
2. **Open the Cloned directory**
     Before Training the model and inferencing with .pt file ,and clone the yolo8 series from the official site or from the github. Use GPU for faster training.

## Dataset 
      Use the below link for data set .
      [link text](https://www.kaggle.com/datasets/ayushv322/animal-classification/data)

## Training
   Use the Main_.ipynb file  to train the yolo model , commonly yolo uses pytorch architecture , so make the cuda environment to run the pytorch.
## Inference
   Use the best.pt for inferencing , elephant_project_live_camera.ipynb file runs the model with live inbuilt camera , if the inference confidence are above .80 the model label the object in the live feed.
   ![Confusion Matrix of four classes](https://github.com/srinath2003/My_Projects/blob/171bb36f6381e8ab76a637b252c75e19e69914a3/Machine_Learning%26Deep_learning/ZEBR_Detector/runs/detect/val/confusion_matrix_normalized.png)
## Usage
   The Model can classify four different animals namely , Elephant , Zebra , Buffalo and Rhino.
   

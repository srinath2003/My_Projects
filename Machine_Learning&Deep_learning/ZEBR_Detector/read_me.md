# Animal Detection

This repository contains a YOLOv8 model trained to detect four animal classes: elephant, zebra, buffalo, and rhino. The model performs real-time detection using a live camera feed.

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
- [Test](#test)
- [Output](#output)
- [Usage](#usage)
- [License](#License)

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
## Test
   Use the best.pt for prediction , elephant_project_live_camera.ipynb file runs the model with live inbuilt camera , if the inference confidence are above .80 the model label the object in the live feed.
   ![Confusion Matrix of four classes](https://github.com/srinath2003/My_Projects/blob/171bb36f6381e8ab76a637b252c75e19e69914a3/Machine_Learning%26Deep_learning/ZEBR_Detector/runs/detect/val/confusion_matrix_normalized.png)
## Output
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/ele1)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/ele2)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/image00)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/image01)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/image31)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/image30)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/image_31)
   ![imes](https://github.com/srinath2003/My_Projects/blob/main/Machine_Learning%26Deep_learning/ZEBR_Detector/Output_with_live_cam/image_1_0)
## Usage
   The Model can classify four different animals namely , Elephant , Zebra , Buffalo and Rhino.

## License
   MIT License
===========

© [2023] [github.com/srinath2003/]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

   

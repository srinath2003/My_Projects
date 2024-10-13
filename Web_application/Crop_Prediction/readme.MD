# Crop Prediction Model

This project is a machine learning-based web application that predicts the most suitable crop to grow based on soil and environmental conditions. The model is built using a Random Forest Classifier and is trained on a dataset of various crops and their growth conditions.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model](#model)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This project uses the `RandomForestClassifier` from the `sklearn` library to predict crops based on factors such as:
- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH level
- Rainfall

The trained model is deployed in a web application using Flask, allowing users to input soil conditions and environmental data to receive crop recommendations.

## Features

- Machine learning model trained on crop data.
- Flask-based web application with a user-friendly interface.
- Predicts the best crop based on user input.
- Displays a confusion matrix heatmap to evaluate model performance.

## Dataset

The dataset used in this project is `Crop_recommendation.csv`, which includes features such as:
- N (Nitrogen in soil)
- P (Phosphorus in soil)
- K (Potassium in soil)
- Temperature
- Humidity
- pH level
- Rainfall

The target variable is the type of crop that grows best under those conditions.

## Model

The model used in this project is a `RandomForestClassifier`. The key steps involved in training the model are:

1. Data preprocessing: Standardization of the input features.
2. Splitting the dataset into training and testing sets.
3. Training the `RandomForestClassifier` on the training data.
4. Evaluating the model on the test data.

The model achieved an accuracy of **99.3%**.

## Web Application

The web application allows users to input the following values:
- Nitrogen, Phosphorus, and Potassium ratios
- Temperature in Celsius
- Humidity percentage
- pH level (0-14 scale)
- Rainfall in millimeters

Based on this input, the application predicts the most suitable crop.

### Example Usage:

The Predicted Crop is rice

## Installation

### Prerequisites

- Python 3.6 or above
- Flask
- Scikit-learn
- Pandas
- Numpy
- Matplotlib
- Seaborn

### Clone the Repository

```bash
git clone https://github.com/srinath2003/My_Projects.git
cd My_Projects/Machine_Learning&Deep_learning/Crop_Prediction
```

## Install Required Packages
``` bash
pip install -r requirements.txt
```

## Run the Flask App
``` bash
python app.py
```
Visit http://127.0.0.1:5000/ to interact with the app.

## Usage
Open the web application in your browser.
Enter the required input values (Nitrogen, Phosphorus, Potassium, temperature, etc.).
Click on "Predict" to see the crop prediction.
## Results
The model was trained on the crop dataset and achieved the following metrics:
Accuracy: 99.3%
![Alt Text]('https://github.com/srinath2003/My_Projects/edit/main/Web_application/Crop_Prediction/results/result.png')
![Alt Text]('https://github.com/srinath2003/My_Projects/edit/main/Web_application/Crop_Prediction/results/result1.png')


The confusion matrix is displayed using a heatmap to visualize the model's performance.
## Future Improvements
Add more features to the model, such as soil type, location, and season.
Integrate with a larger, real-time dataset to improve accuracy.
Deploy the web application on cloud platforms like AWS or Heroku.
## License
This project is licensed under the MIT License.

## Acknowledgments
The dataset used in this project was provided by [https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset].
Special thanks to the open-source libraries that made this project possible.

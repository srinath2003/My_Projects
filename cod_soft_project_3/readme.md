# Iris Dataset Machine Learning Project

This project involves building and evaluating a machine learning model for the Iris dataset. The Iris dataset is a classic dataset in machine learning, containing measurements of various features of iris flowers.

## Table of Contents

- [Introduction](#introduction)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Building and Evaluation](#model-building-and-evaluation)
- [Contributors](#contributors)
- [License](#license)

## Introduction

The Iris dataset is loaded from a CSV file (`IRIS.csv`). The goal is to predict the species of iris flowers based on their features such as sepal length, sepal width, petal length, and petal width.

## Exploratory Data Analysis

- Scatter plots are used to visualize the relationships between different features.
- Pair plots are used to visualize the pairwise relationships between features and to observe how they are distributed across different species.
- Histograms and distribution plots are used to visualize the distribution of each feature.

## Model Building and Evaluation

- The dataset is split into training and testing sets using train_test_split from scikit-learn.
- Three different classifiers are used: Support Vector Machine (SVM), Logistic Regression, and Random Forest.
- The SVM model is trained and evaluated using accuracy score, confusion matrix, and classification report.
- ROC curve is plotted to visualize the performance of the SVM model.

## Contributors

- [Srinath](mailto:srinathranganathan432@email.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

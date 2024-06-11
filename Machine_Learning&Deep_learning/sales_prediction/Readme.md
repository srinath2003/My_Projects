# Sales Prediction Project

## Overview
This project aims to predict sales based on advertising expenditures across multiple channels like TV, Radio, and Newspaper. It utilizes a dataset containing information about advertising budget and corresponding sales figures. The prediction is performed using a multiple linear regression model.

## Dataset
The dataset used in this project is sourced from a CSV file named `advertising.csv`. It contains the following columns:
- TV: Advertising budget spent on TV commercials (in thousands of dollars)
- Radio: Advertising budget spent on Radio commercials (in thousands of dollars)
- Newspaper: Advertising budget spent on Newspaper advertisements (in thousands of dollars)
- Sales: Sales figures (in thousands of units)

## Tools and Libraries Used
- Python: Programming language used for data analysis and model development.
- Pandas: Library used for data manipulation and analysis.
- Matplotlib and Seaborn: Libraries used for data visualization.
- Statsmodels: Library used for building statistical models like linear regression.
- Scikit-learn: Library used for data preprocessing and model evaluation.

## Project Workflow
1. **Data Loading and Exploration**: Load the dataset and perform initial exploration to understand its structure and contents. Check for any missing values or outliers.

2. **Data Visualization**: Visualize the data to gain insights into the relationships between different variables and their distributions.

3. **Data Preprocessing**: Prepare the data for model training by splitting it into features (advertising budgets) and target (sales) variables. Perform any necessary preprocessing steps such as scaling or encoding categorical variables.

4. **Model Training**: Train a multiple linear regression model using the training dataset. Evaluate the model's performance on the training set using metrics like R-squared and Adjusted R-squared.

5. **Model Evaluation**: Evaluate the trained model on the test dataset to assess its generalization performance. Use metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

6. **Sales Prediction**: Utilize the trained model to make sales predictions based on new advertising expenditure inputs provided by the user.

## Files Included
- `advertising.csv`: CSV file containing the dataset.
- `sales_prediction.ipynb`: Jupyter Notebook containing the Python code for data analysis, model development, and predictions.
- `README.md`: This file providing an overview of the project, its objectives, and the workflow.

## How to Use
1. Clone the repository to your local machine.
2. Open and run the `sales_prediction.ipynb` notebook using Jupyter or any compatible environment.
3. Follow the instructions in the notebook to load the dataset, analyze the data, train the model, and make sales predictions.

## Author
[Srinath2003]
[srinathranganathan432@gmail.com]

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

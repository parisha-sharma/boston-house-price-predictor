# 🏠 Boston House Price Predictor

A machine learning web application built using Flask that predicts house prices in Boston using Linear Regression trained on the Boston Housing dataset.

## 🚀 Features
- Predicts house price using 13 key housing features.
- Fully interactive frontend using HTML + CSS.
- Flask backend for ML model integration.
- Easy and clean UI for user inputs.

## 🔧 Tech Stack
- Python 3.12
- Jupyter Notebook
- scikit-learn
- Flask
- HTML/CSS (for frontend)

## 📁 Project Structure
📦BostonHousePricePredictor
    ┣ 📜app.py
    ┣ 📜model_training.ipynb
    ┣ 📜requirements.txt
    ┣ 📜BostonHousing.csv
    ┣ 📂templates
        ┃ ┗ 📜index.html
    ┣ 📂static
        ┃ ┗ 📜style.css

## 🧠 How it Works
1. `model_training.ipynb` trains a Linear Regression model
2. `app.py` loads the trained model
3. Frontend form in `index.html` collects user input
4. Model predicts and displays the house price


from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

# Original features
features = ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age',
            'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']

# User-friendly labels
labels = {
    'crim': 'Crime Rate (per capita)',
    'zn': 'Residential Land Zoned (%)',
    'indus': 'Non-Retail Business Area (%)',
    'chas': 'Charles River (1 if yes, 0 if no)',
    'nox': 'Nitric Oxide Concentration (ppm)',
    'rm': 'Avg. Rooms per Dwelling',
    'age': 'Proportion of Old Units (%)',
    'dis': 'Distance to Employment Centers',
    'rad': 'Accessibility to Highways',
    'tax': 'Property Tax Rate',
    'ptratio': 'Pupil-Teacher Ratio',
    'b': 'Proportion of Black Population',
    'lstat': 'Lower Status Population (%)'
}

@app.route('/')
def home():
    return render_template('index.html', features=features, labels=labels)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(request.form[feature]) for feature in features]
        prediction = model.predict([input_data])[0]
        prediction = round(prediction, 2)
        return render_template('index.html', features=features, labels=labels, prediction=prediction)
    except:
        return render_template('index.html', features=features, labels=labels, prediction="Error")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

features = ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age',
            'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']

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

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    user_input = {}

    if request.method == 'POST':
        try:
            user_input = {feature: request.form[feature] for feature in features}
            input_data = [float(user_input[feature]) for feature in features]
            prediction = round(model.predict([input_data])[0], 2)
        except:
            prediction = "Error"

    return render_template('index.html', features=features, labels=labels, prediction=prediction, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)

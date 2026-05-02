from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model package
pkg     = joblib.load('model.pkl')
model   = pkg['model']
scaler  = pkg['scaler']
selector= pkg['selector']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the HTML form
    features = [
        float(request.form['OverallQual']),
        float(request.form['GrLivArea']),
        float(request.form['GarageCars']),
        float(request.form['TotalBsmtSF']),
        float(request.form['FullBath']),
        float(request.form['YearBuilt']),
        float(request.form['YearRemodAdd']),
        float(request.form['LotArea']),
    ]

    # Apply same preprocessing as training
    features_array = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features_array)

    # Predict (model outputs log price, so we reverse with expm1)
    log_prediction = model.predict(features_scaled)
    prediction = int(np.expm1(log_prediction)[0])

    return render_template('index.html',
        prediction=f"Predicted Sale Price: ${prediction:,}")

if __name__ == '__main__':
    app.run(debug=True)
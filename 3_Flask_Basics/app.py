from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
with open("svm_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return "✅ Diabetes Predictor API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Example request: { "data": [5,166,72,19,175,25.8,0.587,51] }
        input_data = request.get_json()["data"]
        input_array = np.array(input_data).reshape(1, -1)
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]

        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


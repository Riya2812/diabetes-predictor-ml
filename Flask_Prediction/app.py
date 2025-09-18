from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values safely
        pregnancies = int(request.form.get('pregnancies', 0))
        glucose = int(request.form.get('glucose', 0))
        bp = int(request.form.get('bp', 0))
        skin = int(request.form.get('skin', 0))
        insulin = int(request.form.get('insulin', 0))
        bmi = float(request.form.get('bmi', 0))
        dpf = float(request.form.get('dpf', 0))
        age = int(request.form.get('age', 0))

        # Dummy prediction logic (replace with ML model later)
        if glucose > 125:
            prediction = "Diabetic"
        else:
            prediction = "Not Diabetic"

        return render_template(
            'result.html',
            prediction_text=f"The person is {prediction}"
        )

    except Exception as e:
        return render_template(
            'result.html',
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)

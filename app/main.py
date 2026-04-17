from flask import Flask, request, render_template, jsonify
from app.model_loader import init_models, get_pipeline, get_label_encoder
from ml.predict import predict

app = Flask(__name__)

init_models()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        input_data = {
            "Age": int(request.form.get("age", 0)),
            "Gender": request.form.get("gender"),
            "Blood Type": request.form.get("blood_type"),
            "Medical Condition": request.form.get("medical_condition"),
            "Insurance Provider": request.form.get("insurance_provider"),
            "Billing Amount": float(request.form.get("billing_amount", 0)),
            "Admission Type": request.form.get("admission_type"),
            "Medication": request.form.get("medication"),
        }

        result = predict(input_data, get_pipeline(), get_label_encoder())
        print(result)
    return render_template("index.html", result=result)

@app.route("/predict", methods=["POST"])
def api_predict():
    body = request.get_json()

    input_data = {
        "Age": body['Age'],
        "Gender": body["Gender"],
        "Blood Type": body["Blood Type"],
        "Medical Condition": body["Medical Condition"],
        "Insurance Provider": body["Insurance Provider"],
        "Billing Amount": body["Billing Amount"],
        "Admission Type": body["Admission Type"],
        "Medication": body["Medication"],
    }

    result = predict(input_data, get_pipeline(), get_label_encoder())
    return jsonify({"predicted_test_result": result})


if __name__ == "__main__":
    app.run(debug=True)
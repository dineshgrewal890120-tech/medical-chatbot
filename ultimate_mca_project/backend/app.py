from flask import send_from_directory
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify([
        {"disease":"Flu","probability":80,"advice":"Rest and hydration"},
        {"disease":"Cold","probability":60,"advice":"Take warm fluids"},
        {"disease":"Migraine","probability":40,"advice":"Avoid stress"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

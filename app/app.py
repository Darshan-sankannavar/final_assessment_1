import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)  # Fix incorrect use of `name`

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return "Welcome to the final_assessment!"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse JSON data
        data = request.json
        features = data.get("features")
        
        if not features or not isinstance(features, list):
            return jsonify({"error": "Invalid input. 'features' must be a list."}), 400
        
        # Perform prediction
        prediction = model.predict([features])
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

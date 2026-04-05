from flask import Flask, request, jsonify
from flask_cors import CORS  # Essential for connecting Frontend to Backend
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app) 
model = joblib.load('placement_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the frontend
    data = request.get_json(silent= True)
    print(f"1. Data received: {data}")
    try:
        
        input_df = pd.DataFrame([{
            'CGPA': float(data.get('CGPA', 0)),
            'Internships': int(data.get('Internships', 0)),
            'Projects': int(data.get('Projects', 0)),
            'Workshops': int(data.get('Workshops', 0)),
            'AptitudeTestScore': int(data.get('AptitudeTestScore', 0)),
            'SoftSkillsRating': float(data.get('SoftSkillsRating', 0)),
            'PlacementTraining': 1 if(data.get('PlacementTraining') == 'Yes') else 0
        }])

        prob = model.predict_proba(input_df)[0][1]
        percentage = round(prob * 100, 2)

        return jsonify({
            "probability": percentage,
            "status": "Placed" if percentage > 50 else "Not Placed"
        })
    except Exception as e:
        print(f"!!! REAL ERROR: {e}")
        return jsonify({"error": str(e)}), 400 

if __name__ == '__main__':

    app.run(debug=True, port=5000)

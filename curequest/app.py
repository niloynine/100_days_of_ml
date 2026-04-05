from flask import Flask, request, jsonify
from flask_cors import CORS
from logic import find_diseases_by_symptoms

app = Flask(__name__)
CORS(app)  # Allow cross-origin from frontend

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', [])
    if not symptoms:
        return jsonify({'error': 'No symptoms provided'}), 400

    diseases = find_diseases_by_symptoms(symptoms)
    return jsonify({'possible_diseases': diseases})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

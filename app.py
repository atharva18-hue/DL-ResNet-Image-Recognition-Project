# app.py

from flask import Flask, request, jsonify, send_from_directory
from backend.infer import predict, load_model
from PIL import Image

app = Flask(__name__)

# Load model
checkpoint_path = "backend/checkpoint.pth"
model, device = load_model(checkpoint_path)

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    # Get uploaded file
    file = request.files['file']
    img = Image.open(file.stream).convert('RGB')
    
    # Predict label
    label = predict(model, device, img)
    
    return jsonify({'prediction': label})

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    app.run(debug=True)

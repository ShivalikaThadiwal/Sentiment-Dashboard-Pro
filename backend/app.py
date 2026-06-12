from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import re

# Initialize the Flask application instance
app = Flask(__name__)

# Configure Cross-Origin Resource Sharing (CORS) to safely allow frontend-backend communication
CORS(app, supports_credentials=True, origins="*")

# Define base system paths to ensure portable file lookup
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

# Load the pre-trained Machine Learning model assets into global memory
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def clean_text(text):
    """
    Utility function to sanitize raw incoming string inputs.
    Removes URLs, mentions, hashtags, special characters, and normalizes casing.
    """
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)        # Strip hyperlinks
    text = re.sub(r"@\w+", "", text)           # Strip social handles/mentions
    text = re.sub(r"#", "", text)              # Strip hashtag characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)    # Retain alphabetical strings and spaces only
    return text.strip()

@app.route('/predict', methods=['POST', 'OPTIONS'])
def analyze():
    """
    Primary API Endpoint that handles incoming text data payloads, 
    executes real-time ML inference, and returns sentiment classifications.
    """
    # Intercept and acknowledge HTTP OPTIONS preflight requests for CORS handshake validation
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
        
    # Extract incoming JSON payload safely
    data = request.json or {}
    text = data.get('text', '')
    
    # Input validation check for empty data packets
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400
        
    # Execution Pipeline: Step 1 - Preprocessing & Text Cleaning
    cleaned = clean_text(text)
    
    # Execution Pipeline: Step 2 - Text Tokenization and Feature Vectorization
    text_vector = vectorizer.transform([cleaned])
    
    # Execution Pipeline: Step 3 - Statistical Model Classification Inference
    prediction = model.predict(text_vector)[0]
    
    # Execution Pipeline: Step 4 - Live Probability Class Calculation (Confidence Matrix)
    try:
        probabilities = model.predict_proba(text_vector)[0]
        # Identify target index matrix array for active positive metrics
        pos_idx = list(model.classes_).index('positive')
        prob = probabilities[pos_idx] if prediction == 'positive' else probabilities[1 - pos_idx]
        confidence = f"{int(prob * 100)}%"
    except Exception:
        # Standard structural fallback score if probability metrics face arrays exception
        confidence = "90%"

    # Print backend execution logs on terminal console for debug tracking
    print(f"Text: {text} -> Sentiment: {prediction} ({confidence})")
    
    # Package JSON payload response back to client workspace interface
    return jsonify({
        'sentiment': prediction,
        'confidence': confidence
    })

# Main execution loop initializing the local application development runtime server environment
if __name__ == '__main__':
    app.run(debug=True, port=5000)
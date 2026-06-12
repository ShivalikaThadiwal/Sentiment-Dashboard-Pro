import joblib
import os
import re

# Resolve the absolute base directory path to ensure reliable structural file lookups
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

# Deserialize and load pre-trained binary assets into memory (Decoupled, plug-and-play architecture)
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def clean_text(text):
    """
    Data Preprocessing Pipeline:
    Converts text strings to lowercase and runs regular expressions to strip out noise 
    such as URLs, social media tags, and non-alphabetic entities.
    """
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)     # Strip hyperlinks/URLs from the raw string
    text = re.sub(r"@\w+", "", text)        # Strip account tags/mentions from the text stream
    text = re.sub(r"#", "", text)           # Strip hash symbols to isolate keyword text strings
    text = re.sub(r"[^a-zA-Z\s]", "", text) # Retain pure alphabetic data segments and blank spacing
    return text.strip()                     # Clean trailing blank lines or whitespaces

def get_prediction(user_text):
    """
    Core Classification Wrapper:
    Ingests raw customer feedback strings, standardizes features, extracts sparse 
    token mappings, and invokes model inference.
    """
    # Pipeline Step 1: Execute text data preprocessing and token sanitization
    cleaned = clean_text(user_text)
    
    # Pipeline Step 2: Transform clean token text strings into numerical sparse feature vectors using TF-IDF
    text_vector = vectorizer.transform([cleaned])
    
    # Pipeline Step 3: Compute class assignment vector from the pre-trained evaluation matrix
    prediction = model.predict(text_vector)[0]
    
    return prediction
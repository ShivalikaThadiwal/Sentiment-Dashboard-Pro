import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
data = pd.read_csv(
    "datasetFolder/dataset.csv",
    encoding="latin-1",
    header=None,
    names=["target", "id", "date", "flag", "user", "text"]
)

print("Dataset Loaded Successfully")
print(data.head())

# Keep only target and text columns
data = data[["target", "text"]]

# Convert labels
# 0 = Negative, 4 = Positive
data["sentiment"] = data["target"].map({
    0: "negative",
    4: "positive"
})

# Text Cleaning Function
def clean_text(text):
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove @mentions
    text = re.sub(r"@\w+", "", text)

    # Remove hashtags symbol
    text = re.sub(r"#", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    return text

# Clean text
data["text"] = data["text"].apply(clean_text)

# Features and Labels
X = data["text"]
y = data["sentiment"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_vectorized = vectorizer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)

print("Training Model...")
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save Model and Vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel Saved Successfully!")
print("Files Created:")
print(" - model.pkl")
print(" - vectorizer.pkl")
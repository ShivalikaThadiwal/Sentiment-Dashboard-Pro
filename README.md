# Sentiment Dashboard Pro

Sentiment Dashboard Pro is a full-stack web application designed to analyze text sentiment in real-time. It features a responsive, dark-themed frontend dashboard integrated with a Python-based Flask backend hosting a machine learning pipeline.

---

## 🚀 Features

* **Real-Time Sentiment Analysis:** Instantly predicts sentiment from live text inputs using an optimized Machine Learning pipeline.
* **Interactive Workspace:** A dynamic, modern dark-themed user interface equipped with graph monitors to track sentiment distributions.
* **Secure Authentication:** Built-in portal for secure user onboarding, login, and registration workflows.
* **Robust Backend API:** Lightweight and scalable Flask server architecture managing API routes and incoming predictions.

---

## 📁 Project Structure

The project repository is systematically organized into two primary architectural layers:

### 📦 Backend (Flask & Machine Learning)
* `app.py`: The main backend Flask server script hosting API routing configurations and receiving live inputs.
* `model_helper.py`: A dedicated helper utility containing regex-based text preprocessing and prediction wrapper functions.
* `train.py`: A standalone utility script executed once to build, train, and export the ML pipeline.
* `model.pkl`: Serialized binary file of the pre-trained Logistic Regression algorithm.
* `vectorizer.pkl`: Pre-trained TF-IDF vectorizer configuration that converts text strings into mathematical arrays.
* `requirements.txt`: Lists the exact configuration package versions required to reproduce and execute the backend framework.
* `datasetFolder/`: Contains the structured raw text rows used to clean, train, and evaluate the sentiment analysis model.

### 🎨 Frontend (User Interface)
* `index.html`: The primary marketing gateway landing page featuring product overviews and mock UI cards.
* `dashboard.html`: The core analytics workspace layout where live analysis is executed and tracked via graph monitors.
* `auth.html`: The onboarding portal handling secure user authentication routines like log-in and registration flows.
* `css/`: Directory containing custom stylesheets that control the responsive, dark-themed UI layouts.
* `js/`: Directory housing the asynchronous, event-driven JavaScript that orchestrates dynamic DOM updates and API calls.

---

## 🛠️ Local Setup Instructions

### Prerequisites
Make sure you have **Python 3.x** installed on your system.

### 1. Backend Setup
Run the following commands in your terminal to set up the backend:

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
2. Frontend Setup
Simply open frontend/index.html directly in any modern web browser, or serve it using a local server extension (like Live Server in VS Code) to interact with the dashboard.

🤖 Tech Stack Used
Frontend: HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6, Fetch API)

Backend: Python, Flask

Machine Learning: Scikit-Learn (Logistic Regression, TF-IDF Vectorization), Pandas, Regex

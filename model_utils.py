# model_utils.py
import joblib
import numpy as np
import os

# Paths (these filenames exist in your repo)
FAKE_MODEL_PATH = os.environ.get("FAKE_MODEL_PATH", "fake_news_model.pkl")
FAKE_VEC_PATH   = os.environ.get("FAKE_VEC_PATH", "fake_news_vectorizer.pkl")
SPAM_MODEL_PATH = os.environ.get("SPAM_MODEL_PATH", "spam_model.pkl")
SPAM_VEC_PATH   = os.environ.get("SPAM_VEC_PATH", "spam_vectorizer.pkl")

def load_artifacts():
    """
    Load models and vectorizers for both tasks.
    Returns dict: {"fake": {"model":..., "vec":...}, "spam": {...}}
    """
    artifacts = {}
    # Fake-news
    try:
        artifacts["fake"] = {
            "model": joblib.load(FAKE_MODEL_PATH),
            "vec": joblib.load(FAKE_VEC_PATH)
        }
    except Exception as e:
        artifacts["fake"] = {"model": None, "vec": None, "error": str(e)}

    # Spam
    try:
        artifacts["spam"] = {
            "model": joblib.load(SPAM_MODEL_PATH),
            "vec": joblib.load(SPAM_VEC_PATH)
        }
    except Exception as e:
        artifacts["spam"] = {"model": None, "vec": None, "error": str(e)}

    return artifacts

def predict_single(task_artifact, text):
    """
    task_artifact: dict with keys 'model' and 'vec'
    text: raw text string
    Returns: label, confidence (float 0..1)
    """
    model = task_artifact.get("model")
    vec = task_artifact.get("vec")
    if model is None or vec is None:
        raise RuntimeError("Model or vectorizer not loaded for this task.")

    X = vec.transform([text])  # use provided vectorizer
    # prefer predict_proba
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X)[0]
        idx = int(np.argmax(probs))
        label = model.classes_[idx] if hasattr(model, "classes_") else str(idx)
        conf = float(probs[idx])
    else:
        label = model.predict(X)[0]
        # If no predict_proba, confidence unknown -> set 1.0
        conf = 1.0
    return str(label), float(conf)
 

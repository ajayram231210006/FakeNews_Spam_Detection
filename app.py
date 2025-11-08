# app.py  (overwrite/merge with caution — backup original first)
from flask import Flask, request, jsonify, send_file, render_template
import pandas as pd
import os, time
from werkzeug.utils import secure_filename
from model_utils import load_artifacts, predict_single

# Config
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
LOG_FILE = "logs/uploads.log"
ALLOWED_EXT = {"csv"}
DEFAULT_THRESHOLD = float(os.environ.get("CONF_THRESHOLD", 0.75))

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

# Load artifacts once on startup
ARTIFACTS = load_artifacts()

def allowed_file(fn):
    return "." in fn and fn.rsplit(".",1)[1].lower() in ALLOWED_EXT

@app.route("/")
def index():
    # basic UI page (you already have templates/index.html)
    return render_template("index.html")

@app.route("/meta", methods=["GET"])
def meta():
    # return which tasks are available and any load errors
    summary = {}
    for t, v in ARTIFACTS.items():
        ok = (v.get("model") is not None and v.get("vec") is not None)
        summary[t] = {"loaded": ok}
        if not ok and "error" in v:
            summary[t]["error"] = v["error"]
        if ok and hasattr(v["model"], "classes_"):
            summary[t]["classes"] = list(map(str, v["model"].classes_))
    return jsonify(summary)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"ok", "time": time.ctime()})

@app.route("/predict_text", methods=["POST"])
def predict_text():
    """
    JSON body: {"text": "...", "task": "fake"|"spam", "threshold": 0.8 (optional)}
    """
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error":"Missing 'text' in request body"}), 400
    text = str(data["text"])
    task = data.get("task", "fake").lower()
    thr = float(data.get("threshold", DEFAULT_THRESHOLD))

    if task not in ARTIFACTS:
        return jsonify({"error": f"Unknown task '{task}'. Choose from {list(ARTIFACTS.keys())}"}), 400
    art = ARTIFACTS[task]
    if art.get("model") is None:
        return jsonify({"error": f"Model for task '{task}' not loaded."}), 500

    try:
        label, conf = predict_single(art, text)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    out_label = label if conf >= thr else "uncertain"
    return jsonify({"text": text, "task": task, "prediction": out_label, "confidence": round(conf,4)})

@app.route("/predict_csv", methods=["POST"])
def predict_csv():
    """
    Form-data:
      - file: uploaded CSV
      - task: 'fake' or 'spam' (required)
      - text_col: name of column containing text (default 'text')
      - threshold: float between 0-1 (optional)
    Returns: downloadable CSV file
    """
    if 'file' not in request.files:
        return jsonify({"error":"No file part"}), 400
    file = request.files['file']
    if file.filename == "":
        return jsonify({"error":"No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error":"Only CSV allowed"}), 400

    task = request.form.get("task", "").lower()
    if task not in ARTIFACTS:
        return jsonify({"error": "Missing or invalid 'task' form field. Use 'fake' or 'spam'."}), 400

    art = ARTIFACTS[task]
    if art.get("model") is None:
        return jsonify({"error": f"Model for task '{task}' not loaded."}), 500

    text_col = request.form.get("text_col", "text")
    thr = float(request.form.get("threshold", DEFAULT_THRESHOLD))

    # save upload
    fname = secure_filename(file.filename)
    ts = int(time.time())
    upload_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{ts}_{fname}")
    file.save(upload_path)

    # read csv
    try:
        df = pd.read_csv(upload_path)
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV: {str(e)}"}), 400

    if text_col not in df.columns:
        return jsonify({"error": f"Column '{text_col}' not found in CSV. Available columns: {list(df.columns)}"}), 400

    predictions = []
    confidences = []
    for idx, row in df.iterrows():
        raw = row[text_col]
        if pd.isna(raw) or str(raw).strip() == "":
            predictions.append("empty")
            confidences.append("")
            continue
        try:
            label, conf = predict_single(art, str(raw))
            out_label = label if conf >= thr else "uncertain"
            predictions.append(out_label)
            confidences.append(round(conf,4))
        except Exception as e:
            predictions.append("error")
            confidences.append("")
    
    df_out = df.copy()
    df_out["prediction"] = predictions
    df_out["confidence"] = confidences

    out_name = f"predictions_{task}_{ts}_{fname}"
    out_path = os.path.join(app.config["OUTPUT_FOLDER"], out_name)
    df_out.to_csv(out_path, index=False)

    # append to log
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()}\t{upload_path}\t{out_path}\trows={len(df)}\ttask={task}\n")

    # return file
    return send_file(out_path, mimetype="text/csv", as_attachment=True, download_name=out_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

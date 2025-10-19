

---

# FakeNews_Spam_Detection

**Project:** Fake News & Spam Detection using Machine Learning and NLP

---

## 📁 Project Structure

* `data/` — raw & processed **(ignored from git; stored locally or shared separately)**
* `notebooks/` — Jupyter notebooks (EDA, preprocessing, experiments)
* `src/` — scripts (`preprocess.py`, training scripts, etc.)
* `reports/` — dataset summary, sample rows, slides
* `.gitignore` — files/folders excluded from git
* `requirements.txt` — Python packages (generate using `pip freeze`)

---

## ⚙️ How to Set Up (for Teammates)

### 1. Clone the repository

```bash
git clone https://github.com/ajayram231210006/FakeNews_Spam_Detection.git
cd FakeNews_Spam_Detection
```

---

### 2. Get the data

Processed and raw data are **not** in the repository.
Download the datasets and place them in:

```
data/raw/
```

#### 📦 Data sharing

Processed data (cleaned CSVs) are available on Google Drive:
[Download here](https://drive.google.com/file/d/1jIIusWgOHIVbW30oRrbHZ0e29gZ-fkah/view?usp=sharing)

---

### 3. Create virtual environment & install dependencies

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

### 4. Run preprocessing

```bash
python src\preprocess.py
```

---

## 👥 Contact

**Ajayram** — Member A
*Roles:* Data collection, preprocessing, EDA

---


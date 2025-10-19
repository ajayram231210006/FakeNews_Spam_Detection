\# FakeNews\_Spam\_Detection



Project: Fake News \& Spam Detection using Machine Learning and NLP



\## Project structure

\- `data/` - raw \& processed \*\*(ignored from git; stored locally or shared separately)\*\*

\- `notebooks/` - Jupyter notebooks (EDA, preprocessing, experiments)

\- `src/` - scripts (preprocess.py, train scripts)

\- `reports/` - dataset summary, sample rows, slides

\- `.gitignore` - files/folders excluded from git

\- `requirements.txt` - Python packages (generate with pip freeze)



\## How to set up (for teammates)

1\. Clone the repo:

git clone https://github.com/ajayram231210006/FakeNews_Spam_Detection.git

cd FakeNews\_Spam\_Detection





2\. Get the data:

\- Processed and raw data are \*\*not\*\* in the repo. Download the datasets and put them in:

&nbsp; ```

&nbsp; data/raw/

&nbsp; ```

&nbsp; (or ask Ajayram for the Drive link)

## Data sharing
Processed data (cleaned CSVs) are on Google Drive:
https://drive.google.com/file/d/1jIIusWgOHIVbW30oRrbHZ0e29gZ-fkah/view?usp=sharing



3\. Create virtual env \& install deps:

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt





4\. Run preprocessing:

python src\\preprocess.py





\## Contact

Ajayram — Member A (Data collection, preprocessing, EDA)






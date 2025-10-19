import re
import os
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

STOP = set(stopwords.words('english'))
LEM = WordNetLemmatizer()

def clean_text(txt):
    """Lowercase, remove special chars, stopwords, lemmatize."""
    if pd.isna(txt):
        return ""
    txt = str(txt).lower()
    txt = re.sub(r'http\S+|www\S+', ' ', txt)
    txt = re.sub(r'\S+@\S+', ' ', txt)
    txt = re.sub(r'<.*?>', ' ', txt)
    txt = re.sub(r'[^a-z0-9\s]', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    tokens = txt.split()
    tokens = [t for t in tokens if t not in STOP]
    tokens = [LEM.lemmatize(t) for t in tokens]
    return " ".join(tokens)

def process_file(in_path, out_path):
    """Clean text and standardize labels if needed."""
    print(f"\n🔹 Processing: {in_path}")
    df = pd.read_csv(in_path, encoding='latin1', engine='python')

    # Standardize SMS Spam dataset labels
    if 'label' in df.columns:
        if df['label'].dtype == object:
            # Convert ham/spam → 0/1 if text labels found
            unique_vals = df['label'].unique()
            if set(map(str.lower, unique_vals)) >= {'ham', 'spam'}:
                print("ℹ️  Converting 'ham'/'spam' to numeric labels (0/1)...")
                df['label'] = df['label'].str.lower().map({'ham': 0, 'spam': 1})
                print("✅ Label conversion done.")
            else:
                print("ℹ️  Label column already numeric or different format.")
        else:
            print("ℹ️  Label column already numeric.")
    else:
        print("⚠️  No 'label' column found; skipping label conversion.")

    # Ensure 'text' column exists
    if 'text' not in df.columns:
        raise ValueError(f"'text' column not found in {in_path}")

    # Apply text cleaning
    df['clean_text'] = df['text'].apply(clean_text)
    df = df[df['clean_text'].str.strip() != ""].reset_index(drop=True)

    # Save processed file
    df.to_csv(out_path, index=False)
    print(f"✅ Saved cleaned file: {out_path} ({df.shape[0]} rows)")

if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)
    process_file("data/raw/fake_news.csv", "data/processed/clean_fake_news.csv")

    # Try common SMS dataset names
    for name in ["sms_spam.csv", "SMSSpamCollection", "sms_spam_unified.csv"]:
        sms_path = os.path.join("data/raw", name)
        if os.path.exists(sms_path):
            process_file(sms_path, "data/processed/clean_sms_spam.csv")
            break
    else:
        print("⚠️  No SMS file found in data/raw. Please check filename.")

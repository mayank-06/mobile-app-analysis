# src/data_cleaning.py
import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_google(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Standardize column names
    df.columns = [c.strip() for c in df.columns]
    # Drop exact duplicate rows
    df = df.drop_duplicates()
    # drop rows without App or Category
    if 'App' in df.columns and 'Category' in df.columns:
        df = df.dropna(subset=['App','Category'])
    # Clean Installs: "1,000,000+" -> 1000000
    if 'Installs' in df.columns:
        df['Installs'] = df['Installs'].astype(str).str.replace(r'[+,]','', regex=True)
        df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce').fillna(0).astype(int)
    else:
        df['Installs'] = 0
    # Clean Price: "$2.99" -> 2.99
    if 'Price' in df.columns:
        df['Price'] = df['Price'].astype(str).str.replace(r'[$,]','', regex=True)
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0.0)
    else:
        df['Price'] = 0.0
    # Size -> MB
    def size_to_mb(x):
        if pd.isna(x): return np.nan
        x = str(x).strip()
        if x.lower() in ['varies with device','-','unknown','']:
            return np.nan
        try:
            if x.endswith('M'):
                return float(x[:-1])
            if x.endswith('k'):
                return float(x[:-1]) / 1024.0
            return float(x)
        except:
            return np.nan
    if 'Size' in df.columns:
        df['SizeMB'] = df['Size'].apply(size_to_mb)
    else:
        df['SizeMB'] = np.nan
    # Rating numeric
    if 'Rating' in df.columns:
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    else:
        df['Rating'] = np.nan
    # Reviews -> numeric (if exists)
    if 'Reviews' in df.columns:
        df['Reviews'] = pd.to_numeric(df['Reviews'].astype(str).str.replace(',',''), errors='coerce').fillna(0).astype(int)
    else:
        df['Reviews'] = 0
    # Monetization flags
    df['IsPaid'] = (df['Price'] > 0).astype(int)
    # HasIAP: check common column names
    has_iap_cols = [c for c in df.columns if 'in-app' in c.lower() or 'inapp' in c.lower() or 'iap' in c.lower()]
    if has_iap_cols:
        df['HasIAP'] = df[has_iap_cols[0]].notna().astype(int)
    else:
        df['HasIAP'] = 0
    # Derived logs
    df['log_installs'] = np.log1p(df['Installs'].astype(float))
    return df

def clean_apple(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    df = df.drop_duplicates()
    # Common apple columns: 'price', 'user_rating', 'size_bytes', 'rating_count_tot', 'prime_genre', 'track_name'
    # Price
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)
    elif 'Price' in df.columns:
        df['price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0.0)
    else:
        df['price'] = 0.0
    # Rating
    if 'user_rating' in df.columns:
        df['user_rating'] = pd.to_numeric(df['user_rating'], errors='coerce')
    elif 'rating' in df.columns:
        df['user_rating'] = pd.to_numeric(df['rating'], errors='coerce')
    else:
        df['user_rating'] = np.nan
    # Size bytes -> MB
    if 'size_bytes' in df.columns:
        df['size_mb'] = pd.to_numeric(df['size_bytes'], errors='coerce')/1e6
    else:
        df['size_mb'] = np.nan
    # Reviews / rating count
    if 'rating_count_tot' in df.columns:
        df['rating_count'] = pd.to_numeric(df['rating_count_tot'], errors='coerce').fillna(0).astype(int)
    else:
        possible = [c for c in df.columns if 'rating' in c.lower() and 'count' in c.lower()]
        if possible:
            df['rating_count'] = pd.to_numeric(df[possible[0]], errors='coerce').fillna(0).astype(int)
        else:
            df['rating_count'] = 0
    # Monetization flags
    df['IsPaid'] = (df['price'] > 0).astype(int)
    # category name unify
    if 'prime_genre' in df.columns:
        df['Category'] = df['prime_genre']
    elif 'primeGenre' in df.columns:
        df['Category'] = df['primeGenre']
    elif 'genre' in df.columns:
        df['Category'] = df['genre']
    else:
        df['Category'] = 'Unknown'
    df['log_installs'] = np.nan  # Apple dataset often doesn't have installs
    return df

def main():
    # Load files (safe reading)
    google_path = DATA_DIR / "google_playstore.csv"
    apple_path = DATA_DIR / "apple_store.csv"
    if not google_path.exists() and not apple_path.exists():
        print("Place google_playstore.csv and/or apple_store.csv into the data/ folder.")
        return

    if google_path.exists():
        gp = pd.read_csv(google_path, encoding='utf-8', low_memory=False)
        gp_clean = clean_google(gp)
        gp_clean.to_csv(OUT_DIR / "cleaned_google.csv", index=False)
        print("Saved cleaned_google.csv")
    if apple_path.exists():
        ap = pd.read_csv(apple_path, encoding='utf-8', low_memory=False)
        ap_clean = clean_apple(ap)
        ap_clean.to_csv(OUT_DIR / "cleaned_apple.csv", index=False)
        print("Saved cleaned_apple.csv")

if __name__ == "__main__":
    main()
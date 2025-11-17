# src/profiles.py
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"

def cluster_google(path, n_clusters=5):
    gp = pd.read_csv(path, low_memory=False)
    # select features that exist
    use_cols = []
    if 'log_installs' in gp.columns: use_cols.append('log_installs')
    if 'Rating' in gp.columns: use_cols.append('Rating')
    if 'Price' in gp.columns: use_cols.append('Price')
    if 'Reviews' in gp.columns: use_cols.append('Reviews')
    if 'SizeMB' in gp.columns: use_cols.append('SizeMB')
    if not use_cols:
        print("No usable columns for clustering.")
        return gp
    X = gp[use_cols].fillna(0)
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    gp['cluster'] = kmeans.fit_predict(Xs)
    # summary
    summary = gp.groupby('cluster').agg({
        'Installs':'median' if 'Installs' in gp.columns else 'count',
        'Rating':'median' if 'Rating' in gp.columns else 'count',
        'Price':'median' if 'Price' in gp.columns else 'count',
        'App':'count' if 'App' in gp.columns else 'size'
    }).rename(columns={ 'App':'count' })
    print("Cluster summary:")
    print(summary)
    gp.to_csv(OUT_DIR / "gp_clustered.csv", index=False)
    return gp

def main():
    gp_path = ROOT / "outputs" / "cleaned_google.csv"
    if not gp_path.exists():
        print("Run data_cleaning.py first to produce cleaned_google.csv")
        return
    gp = cluster_google(gp_path, n_clusters=5)
    print("Saved gp_clustered.csv to outputs/")

if __name__ == "__main__":
    main()
# src/eda_plots.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set(style="whitegrid")

def plot_google_summary(path):
    gp = pd.read_csv(path, low_memory=False)
    # Top categories by median installs
    if 'Category' in gp.columns and 'Installs' in gp.columns:
        med = gp.groupby('Category')['Installs'].median().sort_values(ascending=False).head(20)
        plt.figure(figsize=(10,7))
        sns.barplot(x=med.values, y=med.index)
        plt.xlabel("Median Installs")
        plt.title("Top 20 Categories by Median Installs (Google)")
        plt.tight_layout()
        plt.savefig(OUT_DIR / "gp_top_categories_installs.png")
        plt.close()
    # Rating distribution
    if 'Rating' in gp.columns:
        plt.figure(figsize=(7,5))
        gp['Rating'].dropna().hist(bins=30)
        plt.title("Google Play Ratings Distribution")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(OUT_DIR / "gp_rating_dist.png")
        plt.close()
    # Price vs Rating (sample)
    if 'Price' in gp.columns and 'Rating' in gp.columns:
        sample = gp.sample(min(3000, len(gp)), random_state=1)
        plt.figure(figsize=(7,5))
        sns.scatterplot(x='Price', y='Rating', data=sample, alpha=0.4)
        plt.title("Price vs Rating (sample)")
        plt.tight_layout()
        plt.savefig(OUT_DIR / "gp_price_vs_rating.png")
        plt.close()

def plot_apple_summary(path):
    ap = pd.read_csv(path, low_memory=False)
    # Category counts
    if 'Category' in ap.columns:
        topc = ap['Category'].value_counts().head(20)
        plt.figure(figsize=(10,7))
        sns.barplot(x=topc.values, y=topc.index)
        plt.title("Top 20 Categories (Apple)")
        plt.tight_layout()
        plt.savefig(OUT_DIR / "ap_top_categories.png")
        plt.close()
    # Ratings histogram
    if 'user_rating' in ap.columns:
        plt.figure(figsize=(7,5))
        ap['user_rating'].dropna().hist(bins=30)
        plt.title("Apple Ratings Distribution")
        plt.tight_layout()
        plt.savefig(OUT_DIR / "ap_rating_dist.png")
        plt.close()

def main():
    gp_clean = OUT_DIR.parent / "outputs" / "cleaned_google.csv"
    ap_clean = OUT_DIR.parent / "outputs" / "cleaned_apple.csv"
    # sometimes path differs; check both
    gp_path = OUT_DIR.parent / "cleaned_google.csv"
    ap_path = OUT_DIR.parent / "cleaned_apple.csv"
    # try common locations
    if (OUT_DIR.parent / "outputs" / "cleaned_google.csv").exists():
        gp_path = OUT_DIR.parent / "outputs" / "cleaned_google.csv"
    if (OUT_DIR.parent / "outputs" / "cleaned_apple.csv").exists():
        ap_path = OUT_DIR.parent / "outputs" / "cleaned_apple.csv"

    # If files exist in outputs
    if gp_path.exists():
        plot_google_summary(gp_path)
        print("Google plots saved.")
    else:
        # try direct outputs/cleaned_google.csv
        p = OUT_DIR / "cleaned_google.csv"
        if p.exists():
            plot_google_summary(p)
            print("Google plots saved.")
        else:
            print("cleaned_google.csv not found; run data_cleaning.py first.")
    if ap_path.exists():
        plot_apple_summary(ap_path)
        print("Apple plots saved.")
    else:
        p = OUT_DIR / "cleaned_apple.csv"
        if p.exists():
            plot_apple_summary(p)
            print("Apple plots saved.")
        else:
            print("cleaned_apple.csv not found; run data_cleaning.py first.")

if __name__ == "__main__":
    main()
<p align="center">
  <img src="https://i.imgur.com/waxVImv.png" width="100%" />
</p>

<h1 align="center">📱 Mobile App Store Data Analysis</h1>

<p align="center">
  <img src="https://img.icons8.com/color/96/data-configuration.png" width="110"/>
</p>

<p align="center">
  <b>A complete data-driven analysis of Google Play Store & Apple App Store apps.</b><br/>
Using Python, Pandas, Matplotlib, Seaborn, and Scikit-Learn.
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Data%20Analysis-EDA-green" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen" />
  <img src="https://img.shields.io/badge/Platform-Jupyter Notebook-yellow" />
  <img src="https://img.shields.io/badge/License-MIT-purple" />
</p>

## 🧠 Overview

This project explores **mobile app market trends** using:

✔ Google Play Store Dataset  
✔ Apple App Store Dataset  

The goal is to perform **end-to-end EDA**, find **business insights**, and identify **factors that make an app successful** (e.g., installs, ratings, price model, category trends).

---

## 📊 Features of This Project

### 🔍 **1. Data Cleaning**
- Handling missing values  
- Converting text columns into numeric  
- Cleaning price, installs, reviews  
- Converting size into MB  
- Removing duplicates  

### 📈 **2. Exploratory Data Analysis (EDA)**
- Rating distribution  
- Category-wise installs  
- Price vs Rating  
- Installs vs Rating  
- Boxplots & histograms  
- High-install vs low-install patterns  

### 🤖 **3. App Profiling (Optional Advanced)**
- K-Means Clustering  
- Top profitable categories  
- User behavior insights  
- Market recommendations  

---

## 📂 Folder Structure

```
mobile-app-analysis/
│
├── data/ # raw datasets (ignored in GitHub)
├── outputs/ # cleaned & processed files
├── src/ # all scripts (cleaning, EDA, clustering)
│ ├── data_cleaning.py
│ ├── eda_plots.py
│ └── profiles.py
│
├── notebooks/
│ └── 1_EDA_and_cleaning.ipynb
│
├── README.md
└── requirements.txt
```


---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Pandas-Data%20Handling-yellow">
  <img src="https://img.shields.io/badge/NumPy-Numerical-blue">
  <img src="https://img.shields.io/badge/Matplotlib-Plotting-red">
  <img src="https://img.shields.io/badge/Seaborn-Visualization-green">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML Models-orange">
</p>

---

## 📁 Datasets Used

📌 **Google Play Store Dataset**  
https://www.kaggle.com/datasets/lava18/google-play-store-apps  

📌 **Apple App Store Dataset**  
https://www.kaggle.com/datasets/ramamet4/app-store-apple-data-set-10k-apps

⚠️ Note:  
Raw datasets are **not uploaded to GitHub** due to size limits.  
Download them manually and store inside:
```
mobile-app-analysis/data/
```

---

## 🚀 How to Run This Project

### 1️⃣ Clone repo
```bash
git clone https://github.com/your-username/mobile-app-analysis.git
cd mobile-app-analysis
```
2️⃣ Create virtual environment
```
python -m venv .venv

```
3️⃣ Activate

Windows:
```
.\.venv\Scripts\Activate.ps1

```
4️⃣ Install requirements
```
pip install -r requirements.txt

```
5️⃣ Run Cleaning Script
```
python src/data_cleaning.py

```
6️⃣ Run EDA Plots
```
python src/eda_plots.py

```
7️⃣ View Notebook
```
notebooks/1_EDA_and_cleaning.ipynb

```


👨‍💻 Author
<p align="center"> <b>Mayank (mayank-06)</b> </p> <p align="center"> <a href="https://github.com/mayank-06"> <img src="https://skillicons.dev/icons?i=github" height="50"> </a> &nbsp;&nbsp; <a href="mailto:mayanksunny402@gmail.com"> <img src="https://skillicons.dev/icons?i=gmail" height="50"> </a> &nbsp;&nbsp; <a href="[https://www.linkedin.com/in/your-link-here/](https://www.linkedin.com/in/mayank-bodgujar-b89497319/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bzr2KbXjTRZKq9AFB3hMfSg%3D%3D)"> <img src="https://skillicons.dev/icons?i=linkedin" height="50"> </a> </p>

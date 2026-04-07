# wind-energy-forecasting-hybrid-models
A multi-model wind energy forecasting framework combining aerodynamic (ADM, BEM), time-series (AR, MA, ARMA), and machine learning/deep learning models, achieving high-accuracy power prediction and deployed via an interactive Streamlit application.

# 🌬️ Multi-Model Wind Energy Forecasting using Physical, Statistical, and Deep Learning Techniques

> **High-accuracy wind energy forecasting using hybrid modeling across physics, statistics, and deep learning.**

---

## 📌 Overview

This project presents an **end-to-end wind power forecasting framework** that integrates:

- Physics-based models  
- Statistical time-series methods  
- Machine learning  
- Deep learning architectures  

to predict wind turbine power output from multivariate meteorological data.

The system is designed to address:

- Non-linearity  
- Stochasticity  
- Temporal dependencies  

while enabling **real-time inference via an interactive Streamlit GUI application**.

---

## 🚀 Key Highlights

- Developed **10+ predictive models** across physical, statistical, ML, and DL domains  
- Achieved high-accuracy forecasting with **ANN (MAE: ~0.025, MSE: ~0.0023)**  
- Benchmarked models using **MAE, MSE, and R² metrics**  
- Implemented a **time-series aware preprocessing pipeline**  
- Built and deployed a **Streamlit-based GUI for real-time prediction**  
- Designed a **hybrid modeling approach (ANFIS)** for interpretability + accuracy  

---

## 🧠 Problem Statement

Wind energy is inherently **intermittent and highly non-linear**, making accurate forecasting critical for:

- Grid stability and load balancing  
- Renewable energy integration  
- Operational planning of wind farms  

This project aims to **model and compare multiple forecasting paradigms** to identify the most effective approach for wind power prediction.

---

## 🏗️ System Architecture

- **Data Acquisition** → Meteorological datasets  
- **Data Preprocessing** → Cleaning, scaling, handling missing values  
- **Feature Engineering** → Derived and temporal features  
- **Model Training** → Physical, Statistical, ML, DL models  
- **Model Evaluation** → MAE, MSE, R² comparison  
- **Deployment** → Streamlit-based GUI  

---

## 📊 Dataset

The dataset consists of **multivariate time-series meteorological data**, including:

### 🌪️ Wind Parameters
- Wind Speed (10m, 100m)  
- Wind Direction (10m, 100m)  
- Wind Gusts  

### 🌡️ Meteorological Features
- Temperature (2m)  
- Relative Humidity  
- Dew Point  

### ⚡ Target Variable
- Power Output (kW)  

---

## ⚙️ Data Preprocessing Pipeline

- Missing value handling (interpolation / removal)  
- Outlier detection using statistical thresholds  
- Feature scaling (Z-score normalization)  
- Feature engineering (e.g., wind speed³, derived features)  
- Time-series structuring (lag features, sequential inputs)  
- Chronological train-test split to prevent data leakage  

---

## 🤖 Models Implemented

### 🔹 Physical Models
- Actuator Disk Model (ADM)  
- Blade Element Momentum (BEM)  

### 🔹 Statistical Models
- Auto-Regressive (AR)  
- Moving Average (MA)  
- ARMA  

### 🔹 Machine Learning Models
- Linear Regression  
- Polynomial Regression  
- K-Nearest Neighbors (KNN)  
- Random Forest  

### 🔹 Deep Learning Models
- Artificial Neural Network (ANN)  
- Recurrent Neural Network (RNN)  
- Convolutional Neural Network (CNN)  
- Gated Recurrent Unit (GRU)  

### 🔹 Hybrid Model
- Adaptive Neuro-Fuzzy Inference System (ANFIS)  

---

## 📈 Model Performance Summary

| Model                  | MAE   | MSE    | Remarks |
|------------------------|------|--------|--------|
| AR                     | 0.387 | 0.186 | Poor baseline |
| MA                     | 0.350 | 0.158 | Better than AR |
| ARMA                   | 0.382 | 0.182 | Moderate |
| Linear Regression      | 0.141 | 0.032 | Simple baseline |
| Polynomial Regression  | 0.136 | 0.030 | Captures non-linearity |
| KNN                    | 0.082 | 0.014 | Best ML model |
| Random Forest          | 0.131 | 0.033 | Robust |
| ANN                    | **0.025** | **0.0023** | ⭐ Best overall |
| RNN                    | 0.045 | 0.012 | Strong temporal modeling |
| CNN                    | 0.124 | 0.026 | Feature extraction |
| GRU                    | 0.131 | 0.030 | Sequential modeling |
| ANFIS                  | 0.113 | 0.023 | Interpretable hybrid |

---

## 🧪 Key Insights

- Deep learning models significantly outperform classical approaches  
- ANN achieves the lowest error and best generalization  
- KNN performs best among traditional ML models  
- Polynomial regression captures turbine non-linearity effectively  
- ANFIS balances interpretability with performance  

---

## 🖥️ Deployment

The project is deployed using **Streamlit**, enabling real-time predictions.

### Features:
- Interactive UI for inputting meteorological parameters  
- Real-time wind power prediction  
- Scaler integration for consistent inference  
- Model loading using TensorFlow and joblib  

### ▶️ Run the App

```bash
streamlit run app.py
```

## 🛠️ Tech Stack:
Programming: Python
Libraries: NumPy, pandas, scikit-learn
Deep Learning: TensorFlow / Keras
Visualization: Matplotlib, Seaborn
Deployment: Streamlit
Data Source: Kaggle API

## 📂 Project Structure

```bash
├── data/
│   ├── input_data.csv
│
├── notebooks/
│   ├── ANN.ipynb
│   ├── RNN.ipynb
│
├── models/
│   ├── ann_model.h5
│   ├── scaler.pkl
│
├── app/
│   ├── app.py
│
├── report/
│   ├── Final_Report.pdf
│
└── README.md
```


## 🔮 Future Work
Integration with real-time IoT wind sensor data
Cloud deployment (AWS / GCP)
Advanced architectures (LSTM, Transformers)
Probabilistic forecasting and uncertainty estimation
Digital twin modeling for wind farms

## 🤝 Contributors
Ishaan Yadav
Karthikeya Chanda

## 📜 License
This project is licensed under the MIT License.

## ⭐ Final Note
This project demonstrates a comprehensive multi-paradigm approach to wind energy forecasting, combining domain knowledge (physics) with modern AI techniques, making it highly relevant for Data Science, Machine Learning, and Energy Analytics roles.





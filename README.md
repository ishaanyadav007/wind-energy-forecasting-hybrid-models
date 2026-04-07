# wind-energy-forecasting-hybrid-models
A multi-model wind energy forecasting framework combining aerodynamic (ADM, BEM), time-series (AR, MA, ARMA), and machine learning/deep learning models, achieving high-accuracy power prediction and deployed via an interactive Streamlit application.

**Overview**
This project presents an end-to-end wind power forecasting framework that integrates physics-based models, statistical time-series methods, machine learning, and deep learning architectures to predict wind turbine power output from multivariate meteorological data.

The system is designed to address the non-linearity, stochasticity, and temporal dependencies inherent in wind energy generation, while enabling real-time inference via an interactive GUI application.

**🚀 Key Highlights**
🔹 Developed 10+ predictive models across physical, statistical, ML, and DL domains
🔹 Achieved high-accuracy forecasting with ANN (MAE: ~0.025, MSE: ~0.0023)
🔹 Benchmarked models using MAE, MSE, and R² metrics
🔹 Implemented time-series aware preprocessing pipeline
🔹 Built and deployed a Streamlit-based GUI for real-time prediction
🔹 Designed a hybrid modeling approach (ANFIS) for interpretability + accuracy
🧠 Problem Statement

Wind energy is inherently intermittent and highly non-linear, making accurate forecasting critical for:
Grid stability and load balancing
Renewable energy integration
Operational planning of wind farms

This project aims to model and compare multiple forecasting paradigms to identify the most effective approach for wind power prediction.

🏗️ System Architecture
Data Acquisition → Data Preprocessing → Feature Engineering → Model Training
       ↓                    ↓                     ↓
 Meteorological      Scaling & Cleaning     Temporal Structuring
       ↓
---------------------------------------------------------------
| Physical | Statistical | ML Models | Deep Learning | Hybrid |
---------------------------------------------------------------
       ↓
**Model Evaluation → Best Model Selection → Deployment (Streamlit GUI)**

**📊 Dataset**
The dataset consists of multivariate time-series meteorological data, including:

🌪️ Wind Parameters
Wind Speed (10m, 100m)
Wind Direction (10m, 100m)
Wind Gusts
🌡️ Meteorological Features
Temperature (2m)
Relative Humidity
Dew Point
⚡ Target Variable
Power Output (kW)

**⚙️ Data Preprocessing Pipeline**
✔️ Missing value handling (interpolation / removal)
✔️ Outlier detection using statistical thresholds
✔️ Feature scaling (Z-score normalization)
✔️ Feature engineering (e.g., wind speed³, derived features)
✔️ Time-series structuring (lag features, sequential inputs)
✔️ Chronological train-test split (no data leakage)

**🤖 Models Implemented**
🔹 Physical Models
Actuator Disk Model (ADM)
Blade Element Momentum (BEM)
🔹 Statistical Models
Auto-Regressive (AR)
Moving Average (MA)
ARMA
🔹 Machine Learning Models
Linear Regression
Polynomial Regression
K-Nearest Neighbors (KNN)
Random Forest
🔹 Deep Learning Models
Artificial Neural Network (ANN)
Recurrent Neural Network (RNN)
Convolutional Neural Network (CNN)
Gated Recurrent Unit (GRU)
🔹 Hybrid Model
Adaptive Neuro-Fuzzy Inference System (ANFIS)

**📈 Model Performance Summary**
| Model                 | MAE       | MSE        | Remarks                  |
| --------------------- | --------- | ---------- | ------------------------ |
| AR                    | 0.387     | 0.186      | Poor baseline            |
| MA                    | 0.350     | 0.158      | Better than AR           |
| ARMA                  | 0.382     | 0.182      | Moderate                 |
| Linear Regression     | 0.141     | 0.032      | Simple baseline          |
| Polynomial Regression | 0.136     | 0.030      | Captures non-linearity   |
| KNN                   | 0.082     | 0.014      | Best ML model            |
| Random Forest         | 0.131     | 0.033      | Robust but not optimal   |
| ANN                   | **0.025** | **0.0023** | ⭐ Best overall           |
| RNN                   | 0.045     | 0.012      | Strong temporal modeling |
| CNN                   | 0.124     | 0.026      | Good feature extraction  |
| GRU                   | 0.131     | 0.030      | Sequential modeling      |
| ANFIS                 | 0.113     | 0.023      | Interpretable hybrid     |

**🧪 Key Insights**
✅ Deep learning models significantly outperform classical methods
✅ ANN achieves lowest error and best generalization
✅ KNN performs best among traditional ML models
✅ Polynomial regression captures non-linear turbine characteristics
✅ ANFIS provides interpretability + reasonable accuracy
🖥️ Deployment

The project is deployed using Streamlit, enabling real-time predictions.

**Features:**
Interactive UI for inputting meteorological parameters
Real-time power output prediction
Scaler integration for consistent inference
Model loading using TensorFlow and joblib
▶️ Run the App
streamlit run app.py

**🛠️ Tech Stack**
Programming: Python
Libraries: NumPy, pandas, scikit-learn
Deep Learning: TensorFlow / Keras
Visualization: Matplotlib, Seaborn
Deployment: Streamlit
Data Source: Kaggle API

**📂 Project Structure**
├── data/
│   ├── input data.csv
│   ├── T1.csv
│
├── notebooks/
│   ├── ANN.ipynb
│   ├── RNN.ipynb
│   ├── CNN.ipynb
│   ├── GRU.ipynb
│   ├── RF.ipynb
│   ├── ARIMA/ARMA notebooks
│
├── models/
│   ├── saved models
│   ├── scalers
│
├── app/
│   ├── app.py
│
├── report/
│   ├── Final Report.pdf
│   ├── PPT.pptx
│
└── README.md

**🔮 Future Work**
🔹 Integration with real-time IoT wind sensor data
🔹 Deployment on cloud (AWS / GCP)
🔹 Use of advanced architectures (LSTM, Transformers)
🔹 Probabilistic forecasting (uncertainty quantification)
🔹 Digital twin modeling for wind farms

**🤝 Contributors**
Ishaan Yadav
Karthikeya Chanda

**📜 License**
This project is for academic and research purposes.

**⭐ Final Note**
This project demonstrates a comprehensive, multi-paradigm approach to renewable energy forecasting, combining domain knowledge (physics) with modern AI techniques, making it highly relevant for Data Science, Machine Learning, and Energy Analytics roles.










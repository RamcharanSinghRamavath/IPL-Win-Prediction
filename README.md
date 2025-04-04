# IPL-Win-Prediction

## 📌 Project Overview

The IPL Win Predictor is a machine learning-based web application that predicts the winner of an IPL match based on historical data from 2008 to 2024. The model is trained using past match data and various cricket-specific parameters to provide accurate predictions.

## 🚀 Features

- **Predict IPL match winners** based on team compositions and match conditions.
- **Uses historical IPL data** (2008-2024) for training and evaluation.
- **Machine learning-based approach** using classification models.
- **Stylish web app UI** for easy interaction.
- **Deployed on Streamlit** for accessibility and real-time predictions.

## 💂️ Dataset

The model is trained on **two key IPL datasets**:

1. `matches.csv` – Contains details of IPL matches from 2008 to 2024, including teams, venues, toss details, and match results.
2. `deliveries.csv` – Provides ball-by-ball data for every IPL match, including batsman, bowler, runs, and dismissal information.

## ⚙️ Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **Machine Learning** (Logistic Regression, Random Forest, or XGBoost)
- **Streamlit** (For UI and deployment)
- **Flask** (If additional backend support is required)
- **Jupyter Notebook** (For model development and analysis)

## 📌 How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/RamcharanSinghRamavath/IPL-Win-Predictor.git
   cd IPL-Win-Predictor
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the model notebook:

   ```bash
   jupyter notebook code.ipynb
   ```

4. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## 📊 Model Training & Evaluation

- The model is trained on past IPL match results with features like **team performance, venue factors, and player statistics**.
- Different machine learning algorithms are compared, and the best-performing model (`ipl_win_predictor.pkl`) is used for predictions.

## 📌 Future Enhancements

- Integrating **real-time IPL data** for dynamic predictions.
- Adding **player form and injury updates** for better accuracy.
- Enhancing UI for better user experience.
- Deploying on a **cloud platform** for wider accessibility.

## 📩 Contact

For any queries or collaborations, feel free to reach out:

- 📧 Email: ramcharansinghramavath@gmail.com  
- 🔗 [LinkedIn](https://www.linkedin.com/in/ramavath-ramcharan-singh29/)  
- 🏆 [GitHub](https://github.com/RamcharanSinghRamavath)

---

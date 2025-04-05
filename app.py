# IPL Win Predictor Web App
import streamlit as st
import pandas as pd
import pickle

# Load data
matches = pd.read_csv(r"C:\Users\ramch\Downloads\Ipl Win Predictor\Datasets\matches.csv")
deliveries = pd.read_csv(r"C:\Users\ramch\Downloads\Ipl Win Predictor\Datasets\deliveries.csv")
model = pickle.load(open("ipl_win_predictor.pkl", "rb"))

# IPL Teams & Cities
teams = sorted(matches['team1'].dropna().unique())
cities = sorted(matches['city'].dropna().unique())

# Page Config
st.set_page_config(page_title="IPL Win Predictor", layout="wide")

# Load Custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>🏏 IPL Win Predictor</h1>", unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("⚡ Match Details")
batting_team = st.sidebar.selectbox("🏏 Select Batting Team", teams)
bowling_team = st.sidebar.selectbox("🎯 Select Bowling Team", [team for team in teams if team != batting_team])
city = st.sidebar.selectbox("📍 Select City", cities)

# Match Inputs
target = st.sidebar.number_input("🎯 Target Score", min_value=1)
score = st.sidebar.number_input("🏏 Current Score", min_value=0)
overs = st.sidebar.number_input("⏳ Overs Completed", min_value=0.1, max_value=20.0, step=0.1, format="%.1f")
wickets = st.sidebar.number_input("❌ Wickets Fallen", min_value=0, max_value=9)

# Prediction Logic
if overs > 0 and wickets < 10 and score < target:
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    # Predict
    result = model.predict_proba(input_df)[0]
    win_prob = round(result[1] * 100, 2)

    # Display Result
    st.markdown(f"""
        <div class="result">
            <h2>{batting_team} Win Probability: <span>{win_prob}%</span></h2>
            <div class="bar-container">
                <div class="bar" style="width:{win_prob}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Please ensure overs > 0, wickets < 10, and score < target.")

# Footer
st.markdown("<footer>⚡ Built with ❤️ by Ramcharan Singh Ramavath</footer>", unsafe_allow_html=True)

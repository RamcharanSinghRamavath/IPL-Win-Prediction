# IPL Win Predictor Web App
import streamlit as st
import pandas as pd
import pickle
import os

# ---------- CONFIG ---------- #
st.set_page_config(page_title="IPL Win Predictor", layout="wide")

# ---------- LOAD CSS ---------- #
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- LOAD MODEL & DATA (Cached) ---------- #
@st.cache_resource
def load_model():
    with open("ipl_win_predictor.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    matches = pd.read_csv("Datasets/matches.csv")
    deliveries = pd.read_excel("Datasets/deliveries.xlsx")
    return matches, deliveries

model = load_model()
matches, deliveries = load_data()

# ---------- STATIC DATA ---------- #
teams = sorted(matches['team1'].dropna().unique())
cities = sorted(matches['city'].dropna().unique())

# ---------- TITLE ---------- #
st.markdown("<h1 class='title'>🏏 IPL Win Predictor</h1>", unsafe_allow_html=True)

# ---------- SIDEBAR INPUTS ---------- #
st.sidebar.header("⚡ Match Details")
batting_team = st.sidebar.selectbox("🏏 Select Batting Team", teams)
bowling_team = st.sidebar.selectbox("🎯 Select Bowling Team", [team for team in teams if team != batting_team])
city = st.sidebar.selectbox("📍 Select City", cities)

target = st.sidebar.number_input("🎯 Target Score", min_value=1)
score = st.sidebar.number_input("🏏 Current Score", min_value=0)
overs = st.sidebar.number_input("⏳ Overs Completed", min_value=0.1, max_value=20.0, step=0.1, format="%.1f")
wickets = st.sidebar.number_input("❌ Wickets Fallen", min_value=0, max_value=9)

# ---------- PREDICTION LOGIC ---------- #
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

    # ---------- DISPLAY RESULT ---------- #
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

# ---------- FOOTER ---------- #
st.markdown("<footer>⚡ Built with ❤️ by Ramcharan Singh Ramavath</footer>", unsafe_allow_html=True)

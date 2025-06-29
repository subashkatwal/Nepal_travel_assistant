from urllib import response
from altair import condition
import streamlit as st
import pandas as pd
import joblib


#Weather Suggestion via API 
import requests
def get_weather(city_name,api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},NP&units=metric&appid={api_key}"
    response= requests.get(url)

    if response.status_code== 200:
        data= response.json()
        return{
            "temp":data["main"]["temp"],
            "condition":data["weather"][0]["main"],
            "description": data["weather"][0]["description"]
            }
    else:
        return None


# Load model components
model = joblib.load("../models/model.pkl")
scaler = joblib.load("../models/scaler.pkl")
model_features = joblib.load("../models/features.pkl")

# Load original data to extract categories
df = pd.read_csv("../data/cleaned_destinations.csv")

# Unique input options
categories = sorted(df['category'].unique())
cities = sorted(df['city'].unique())
seasons = sorted(df['best_season'].unique())

# Streamlit UI
st.set_page_config(page_title="Nepal Travel Assistant", layout="centered")

st.title("Nepal Travel Assistant")
st.markdown("Plan your trip with AI-powered cost estimation based on your preferences.")

# Sidebar input
with st.form("trip_form"):
    duration = st.number_input("📅 Duration (in days)", min_value=1, max_value=30, value=3)
    category = st.selectbox("🏕️ Travel Category", categories)
    city = st.selectbox("📍 Destination City", cities)
    season = st.selectbox("🌤️ Preferred Season", seasons)
    submitted = st.form_submit_button("Estimate Trip Cost")

# Feature preparation
def prepare_features(duration, category, city, season):
    features = {col: 0 for col in model_features}
    features['duration_days'] = duration

    cat_col = f"category_{category}"
    city_col = f"city_{city}"
    season_col = f"best_season_{season}"

    for col in [cat_col, city_col, season_col]:
        if col in features:
            features[col] = 1

    df_input = pd.DataFrame([features])
    X_scaled = scaler.transform(df_input)
    return X_scaled

# Prediction and result
if submitted:
    X_user = prepare_features(duration, category, city, season)
    cost = model.predict(X_user)[0]
    st.success(f"🧾 Estimated Trip Cost: **NPR {cost:.2f}**")
    
    weather_api_key= "cfa88cf4f2cc50cf85c1882f0449d0c3"
    weather=get_weather(city,weather_api_key)
    if weather:
        st.info(f"Current weather in city {city}: {weather['temp']}°C, {weather['description'].capitalize()}")

        if weather['condition'].lower() in ['rain','thunderstorm','snow']:
            st.warning("Weather might be not suitable for travel. Consider a different season.")
    if city in df['city'].values:
        best_season= df[df['city']==city]['best_season'].mode().values[0]
        st.markdown(f"Best time to visit { city } is ususally : _{best_season}_")

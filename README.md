# Nepal Travel Assistant

## Project Overview
Nepal Travel Assistant is an ML-powered web application that helps tourists plan personalized travel itineraries across Nepal. By considering user preferences such as budget, interests, trip duration, and real-time weather data, the app recommends optimized travel plans including destination suggestions and estimated trip costs.



## Features
- Destination classification based on user interests (adventure, cultural, nature, trekking, etc.)
- Cost estimation model predicting trip budget based on duration and season
- Personalized itinerary generation tailored to user preferences
- Integration with real-time weather API for destination conditions
- Interactive Streamlit-based web interface for easy user interaction


## Technologies Used
- Python (pandas, numpy, scikit-learn)
- Natural Language Processing for destination categorization (TF-IDF, KMeans)
- Regression models for cost estimation
- Streamlit for frontend web app
- APIs: OpenWeatherMap for weather data, Google Places API (optional)


## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/subashkatwal/nepal-travel-assistant.git
cd nepal-travel-assistant

### 2. Create and activate a virtual environment(Optional)

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the streamlit app
streamlit run app/streamlit_app.py


# Data Sources


# Future work




#Author
Subash Katwal 
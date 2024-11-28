import os
import json
import pandas as pd
import numpy as np
import streamlit as st
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Helper functions for data integration
def load_mock_data(file_path):
    """
    Load and normalize mock health data from a CSV file.
    """
    # Load the data
    mock_data = pd.read_csv(file_path)

    # Normalize the data
    mock_data['date'] = pd.to_datetime(mock_data['date'], format='%m/%d/%Y')

    return mock_data

def save_normalized_data(df, output_dir):
    """
    Save normalized data to CSV and JSON.
    """
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "processed_health_data.json")
    csv_path = os.path.join(output_dir, "processed_health_data.csv")

    # Save JSON and CSV
    df.to_json(json_path, orient="records", lines=True)
    df.to_csv(csv_path, index=False)

    return csv_path

# Load and process the data
mock_file_path = "/Users/emmanuelochiba/PycharmProjects/health-tech-dashboard/MOCK_DATA.csv"  # Ensure your CSV file is in the correct path
output_dir = "./output"
mock_data = load_mock_data(mock_file_path)
normalized_csv_path = save_normalized_data(mock_data, output_dir)

# Streamlit starts here
st.sidebar.title("Mind-Health App")
st.sidebar.markdown("AI-driven insights for health metrics. Powered by **mock data** and **AI models**.")
st.sidebar.markdown("---")

st.title("AI Health Insights Dashboard")

# Load health dataset
@st.cache_data
def load_health_data():
    return pd.read_csv(normalized_csv_path)

health_data = load_health_data()

# Pre-calculate dataset averages for quick insights
average_metrics = {
    "daily_steps": np.mean(health_data["daily_steps"]),
    "daily_calories_burned": np.mean(health_data["daily_calories_burned"]),
    "daily_active_minutes": np.mean(health_data["daily_active_minutes"]),
    "daily_weight_kg": np.mean(health_data["daily_weight_kg"]),
    "daily_sleep_hours": np.mean(health_data["daily_sleep_hours"]),
}

# Load AI models
@st.cache_resource
def load_text_generation_model():
    return pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

@st.cache_resource
def load_sentiment_analysis_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

text_generation_model = load_text_generation_model()
sentiment_analysis_model = load_sentiment_analysis_model()

# Tabs for different AI-driven functionalities
tab1, tab2, tab3 = st.tabs(["Fitness Tracker", "Sleep Analysis", "Sentiment Analysis"])

# Tab 1: Fitness Tracker
with tab1:
    st.subheader("Fitness Tracker")
    st.markdown("Enter your fitness data for actionable insights.")

    # Inputs
    weight = st.number_input('Weight (kg):', min_value=1, step=1)
    steps = st.number_input('Steps Today:', min_value=0, step=1)
    calories = st.number_input('Calories Burned:', min_value=0, step=1)
    active_minutes = st.number_input('Active Minutes:', min_value=0, step=1)

    # Generate insights
    if st.button("Get Fitness Insights"):
        input_text = (f"User has {steps} steps, burned {calories} calories, "
                      f"did {active_minutes} active minutes, and weighs {weight} kg. Provide a fitness tip.")
        with st.spinner("Generating insights..."):
            tip = text_generation_model(input_text)[0]["generated_text"]

        # Visual comparison
        user_data = [steps, calories, active_minutes]
        avg_data = [
            average_metrics["daily_steps"],
            average_metrics["daily_calories_burned"],
            average_metrics["daily_active_minutes"]
        ]
        labels = ["Steps", "Calories", "Active Minutes"]

        st.success(f"Fitness Tip: {tip}")
        st.write("Your metrics vs. dataset averages:")
        fig, ax = plt.subplots()
        ax.bar(labels, user_data, color="blue", alpha=0.6, label="Your Data")
        ax.bar(labels, avg_data, color="green", alpha=0.3, label="Average")
        plt.legend()
        st.pyplot(fig)

        # Downloadable JSON
        result = {"steps": steps, "calories": calories, "active_minutes": active_minutes, "fitness_tip": tip}
        st.download_button(
            label="Download Insights as JSON",
            data=json.dumps(result, indent=4),
            file_name="fitness_insights.json",
            mime="application/json",
        )

# Tab 2: Sleep Analysis
with tab2:
    st.subheader("Sleep Analysis")
    st.markdown("Input your sleep data for personalized recommendations.")

    # Inputs
    sleep_hours = st.number_input("Sleep Duration (hours):", min_value=0, step=1)
    disturbances = st.number_input("Nightly Disturbances:", min_value=0, step=1)

    # Generate insights
    if st.button("Analyze Sleep"):
        input_text = f"User sleeps {sleep_hours} hours and experiences {disturbances} disturbances. Provide tips for improvement."
        with st.spinner("Analyzing sleep patterns..."):
            tip = text_generation_model(input_text)[0]["generated_text"]

        st.success(f"Sleep Tip: {tip}")
        avg_sleep = average_metrics["daily_sleep_hours"]
        st.write(f"Your sleep: **{sleep_hours} hours** (Recommended: 7-9 hours).")
        st.info("Consider adjustments to meet recommended sleep if necessary.") if sleep_hours < avg_sleep else st.success("Great sleep duration!")

        # Downloadable insights
        result = {"sleep_hours": sleep_hours, "disturbances": disturbances, "sleep_tip": tip}
        st.download_button(
            label="Download Sleep Analysis as JSON",
            data=json.dumps(result, indent=4),
            file_name="sleep_analysis.json",
            mime="application/json",
        )

# Tab 3: Journaling Sentiment Analysis
with tab3:
    st.subheader("Journaling Sentiment Analysis")
    st.markdown("Write your thoughts below, and we'll analyze your emotions.")

    # Inputs
    journal_text = st.text_area("Journal Entries (One per line):", height=200)

    if st.button("Analyze Sentiment"):
        if journal_text.strip():
            entries = [line.strip() for line in journal_text.split("\n") if line.strip()]
            sentiments = [{"entry": entry, "sentiment": sentiment_analysis_model(entry)[0]["label"]} for entry in entries]

            # Display results
            st.write("Sentiment Analysis Results:")
            st.table(sentiments)

            # Word cloud
            st.write("Word Cloud of Your Journal:")
            wordcloud = WordCloud(background_color="white").generate(" ".join(entries))
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)

            # Downloadable results
            st.download_button(
                label="Download Sentiment Analysis as JSON",
                data=json.dumps(sentiments, indent=4),
                file_name="sentiment_analysis.json",
                mime="application/json",
            )
        else:
            st.warning("Please provide valid journal entries.")
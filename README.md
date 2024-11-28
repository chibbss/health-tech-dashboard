# AI-Driven Health Insights App

## Overview
This project involves building an AI-powered health insights app that integrates with wearable data, analyzes it using AI models, and generates actionable insights for fitness, sleep, and journaling. The app provides a dashboard for users to interact with, receive personalized health recommendations, and download their insights.

---

## Table of Contents
- [System Architecture](#system-architecture)
- [Implementation Plan](#implementation-plan)
- [Scalability Considerations](#scalability-considerations)
- [Challenges and Mitigation](#challenges-and-mitigation)
- [Setup and Deployment Instructions](#setup-and-deployment-instructions)
  - [Running Locally](#running-locally)
  - [Running on Google Colab](#running-on-google-colab)

---

## System Architecture

### 1. Data Collection (Mockaroo API / Mock Datasets)
Since we couldn't quickly access free APIs for wearable devices, we used **Mockaroo** to generate mock health datasets simulating real-world wearable data (e.g., steps, calories burned, active minutes, weight, sleep duration, disturbances). You can replace this mock data with real-time data from APIs like Fitbit, Google Fit, or Apple Health in the future. Mockaroo's tool can be accessed [here](https://www.mockaroo.com/).

### 2. AI Agents
Three core AI agents power the analysis:
- **Fitness Insights**: Analyzes fitness data (steps, calories, active minutes, weight) and provides actionable tips using the `facebook/blenderbot-400M-distill` model.
- **Sleep Analysis**: Examines user sleep patterns to provide tips for better sleep using the same text-generation model.
- **Journaling Sentiment Analysis**: Processes journal entries and determines the sentiment (positive/negative) using the `distilbert-base-uncased-finetuned-sst-2-english` model.

### 3. Insights Aggregation
The system aggregates insights into actionable recommendations, allowing users to compare their data against averages stored in the system (e.g., daily steps vs. community benchmarks).

### 4. Output Layer (API Endpoints or Dashboard)
The app provides a **Streamlit dashboard** for:
- Interactive data input.
- Visualization of insights and recommendations.
- Downloadable JSON files of insights.

---

## Implementation Plan

### 1. Data Flow from Input to Insights
1. **User Input**: Health data (steps, calories, active minutes, sleep hours, disturbances, journal entries) is entered through the Streamlit dashboard.
2. **Data Storage**: User data is temporarily saved in structured formats (CSV/JSON).
3. **AI Analysis**: The AI models process the data to generate insights.
4. **Output**: Insights are displayed on the dashboard and can be downloaded as JSON.

### 2. Technologies Used
- **Frontend**: Streamlit for building the dashboard.
- **Backend**: Python (Flask or FastAPI for serving AI models).
- **AI Libraries**: Hugging Face Transformers for text generation and sentiment analysis.
- **Visualization**: Matplotlib for graphs and WordCloud for journaling insights.

### 3. Modularity for Adding New AI Agents or Data Sources
- New AI agents (e.g., stress analysis) can be added by extending the existing pipeline.
- Wearable APIs (Fitbit, Apple Health, etc.) can be integrated by modifying the input layer.

---

## Scalability Considerations

1. **Increased Data Volume**:
   - Store user data persistently using databases (e.g., PostgreSQL, MongoDB).
   - Use cloud infrastructure (AWS, GCP) to scale computations.

2. **Additional APIs**:
   - Add connectors to wearable APIs for real-time data.
   - Implement caching and rate-limiting for efficient API usage.

3. **Model Optimization**:
   - Use model quantization for faster inferences.
   - Deploy models on GPUs/TPUs to reduce latency.

---

## Challenges and Mitigation

### 1. Deployment Issues on Streamlit Cloud
- **Error**: Distribution not found at: file:///colabtools/dist/google_colab-1.0.0.tar.gz
ERROR: cudf_cu12-24.10.1-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl is not a supported wheel on this platform.
[notice] A new release of pip is available: 24.0 -> 24.3.1

- **Mitigation**: The issue stems from incompatible dependencies during deployment on Streamlit Cloud. As a workaround, run the app locally or use Google Colab with a tunnel to expose the app.

### 2. Data Consistency
- Normalize data into standard formats (CSV/JSON) and apply validation checks.

### 3. Model Latency
- Use GPUs/TPUs for faster inferences and batch process user requests.

---

## Setup and Deployment Instructions

### Running Locally

1. **Clone the Repository**:
 ```bash
 git clone https://github.com/yourusername/health-insights-app.git
 cd health-insights-app



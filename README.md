# AI-Driven Health Insights App

## Overview
This project involves building an AI-powered health insights app that integrates with wearable data, analyzes it using AI models, and generates actionable insights for fitness, sleep, and journaling. The app provides a dashboard for users to interact with, receive personalized health recommendations, and download their insights.

## Table of Contents
- [System Architecture](#system-architecture)
- [Implementation Plan](#implementation-plan)
- [Scalability Considerations](#scalability-considerations)
- [Challenges and Limitations](#challenges-and-limitations)
- [How to Run the Streamlit App on Google Colab](#how-to-run-the-streamlit-app-on-google-colab)
- [Running Locally](#running-locally)

---

## System Architecture

Below is the high-level system architecture diagram for the **MindHealth App**:

![System Architecture](MINDHEALTH%20APP.png)

### 1. Data Collection (Mockaroo API / Mock Datasets)
Since we couldn't quickly access free APIs for wearable devices, we used **Mockaroo** to generate mock health datasets, which simulate the types of data typically collected from wearables (steps, calories burned, active minutes, weight, sleep duration, and disturbances). The dataset was created with Mockaroo’s online tool, and it’s used here to simulate real-world data in the app. The link to Mockaroo is: [https://www.mockaroo.com/](https://www.mockaroo.com/).

In the future, you can replace this mock data with real-time data from APIs like Fitbit, Google Fit, or Apple Health by integrating them into the data collection layer.

### 2. AI Agents
Three core AI agents power the analysis:
- **Fitness Insights**: Uses user input (steps, calories, active minutes, weight) and provides personalized fitness tips based on an AI text generation model (`facebook/blenderbot-400M-distill`).
- **Sleep Analysis**: Analyzes user sleep patterns and disturbances to provide tips for improving sleep using the same text generation model.
- **Journaling Sentiment Analysis**: Analyzes user-written journal entries and determines the sentiment (positive/negative) using a sentiment analysis model (`distilbert-base-uncased-finetuned-sst-2-english`).

### 3. Insights Aggregation
The system aggregates data insights into actionable recommendations, allowing users to compare their data against the average metrics stored in the system. For instance, comparing daily steps, calories burned, and active minutes against a dataset of averages.

### 4. Output Layer (API Endpoints or Dashboard)
The app provides a user-friendly dashboard built using Streamlit, allowing for:
- Interactive inputs for health data.
- Displaying insights and recommendations.
- Downloadable insights in JSON format.

---

## Implementation Plan

### 1. Data Flow from Input to Insights
- **User Input**: Health data (steps, calories, active minutes, sleep hours, disturbances, journal entries) is input through the Streamlit interface.
- **Data Storage**: User data is saved temporarily and normalized into structured data formats (CSV/JSON).
- **AI Analysis**: Data is processed by AI models (text generation for fitness and sleep, sentiment analysis for journaling) to provide insights.
- **Output**: Insights are displayed on the dashboard, and users can download the insights as JSON files.

### 2. Technologies to Use
- **Frontend**: Streamlit (for building the interactive dashboard).
- **Backend**: Python (Flask or FastAPI for serving AI models).
- **AI Libraries**: Hugging Face Transformers (for text generation and sentiment analysis).
- **Data Storage**: CSV/JSON (temporary storage), potentially integrated with a database in future versions.
- **Visualization**: Matplotlib (for visualizing fitness data), WordCloud (for journaling analysis).

### 3. Modularity for Adding New AI Agents or Data Sources
- **AI Agents**: New AI models or agents (e.g., stress analysis) can be added by extending the current structure with new pipelines.
- **Data Sources**: Additional data sources, such as wearable device APIs, can be integrated by modifying the input layer and data collection methods.

---

## Scalability Considerations

### 1. Handling Increased Data Volume
- **Data Storage**: As the number of users grows, integrating a database (e.g., PostgreSQL, MongoDB) will be necessary to store user data persistently.
- **Model Optimization**: Deploy models using batch processing or offload heavy computations to cloud infrastructure (e.g., AWS, Google Cloud, Azure) for faster processing.

### 2. Integrating Additional Wearable APIs
- Wearable APIs (like Fitbit, Apple Health, or Google Fit) can be integrated by adding connectors that fetch and normalize data from those services.
- Implement rate-limiting and data caching to avoid API request overload.

---

## Challenges and Limitations

### 1. Getting Free Data
- **Challenge**: Access to free APIs for wearable data was unavailable during development.
- **Solution**: A dataset was generated using Mockaroo, simulating real-world wearable data.

### 2. Low-Quality Model Responses
- **Challenge**: The AI models used (e.g., BlenderBot, DistilBERT) are lightweight and not optimized for medical applications.
- **Solution**: While these models provide proof-of-concept functionality, they may not offer high-quality medical insights. Users should expect limited accuracy, and future improvements will involve integrating domain-specific AI models.

### 3. Limited Data
- **Challenge**: The insights are limited to basic metrics, which may not fully represent the complexity of health analysis.
- **Solution**: Future iterations can include more metrics and integrate real-time wearable data.

### 4. Computational Resources
- **Challenge**: Running the app locally without access to a GPU caused slower model loading and processing times.
- **Solution**: The app was tested on Google Colab to leverage free GPU resources. Users may also deploy the app on cloud platforms for better performance.

---

## How to Run the Streamlit App on Google Colab

To run the Streamlit app on Google Colab, follow these steps:

1. **Clone the Repository**: First, clone this repository to your local machine or directly into Google Colab using the following command:

    ```bash
    !git clone https://github.com/yourusername/health-insights-app.git
    ```

2. **Install Dependencies**: Next, install the required dependencies by running the following command:

    ```bash
    !pip install -r health-insights-app/requirements.txt
    ```

3. **Run the Streamlit App**: To run the Streamlit app on Colab, follow the steps in this [Medium article](https://medium.com/@aagamanbhattrai/running-a-streamlit-application-in-google-colab-1576b7188c87). It provides a detailed guide on setting up a tunnel to display the Streamlit app within Colab.

    Be patient, as Google Colab may sometimes experience connectivity issues. If the app doesn't launch immediately, try re-running the command or following the troubleshooting steps from the article.

---

## Running Locally

To run the Streamlit app locally, simply clone the repo to ensure you have the mock dataset if you choose to use it, install dependencies and simply run the app

1. **Clone the Repository**:  
   Clone the repository to your local machine and navigate to the project directory.

   ```bash
   git clone https://github.com/yourusername/health-insights-app.git
   cd health-insights-app



2. **Install Dependencies and run the app**:  
   Install all the required Python dependencies and start the Streamlit app by running the following commands

   ```bash
   pip install -r requirements.txt
   streamlit run app.py

Important Note: Running the app locally may result in slower performance due to loading the AI models on your local computer, which can be resource-intensive. If the models take too long to load or run, consider using a cloud platform or a machine with more computational resources for better performance; which was why I experimented with running it on google colab first due to the GPUs available.


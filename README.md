A proof-of-concept system to integrate, process, and normalize wearable health data (such as steps, heart rate, sleep, HRV) for actionable insights. This project simulates a “Mind-Body Connection Dashboard” that highlights correlations between physical and mental health metrics.

# Health Tech Dashboard

## Description

This project demonstrates the ability to integrate, process, and normalize wearable health data to generate actionable insights. The data includes health metrics such as **steps**, **heart rate**, **sleep**, **heart rate variability (HRV)**, and more. It is designed to simulate a "Mind-Body Connection Dashboard" that correlates physical and mental health metrics.

The project includes the following key components:
1. **Data Integration Layer**: Integrates mock data generated from [Mockaroo](https://mockaroo.com/).
2. **Backend System**: Implements data processing and normalization.
3. **Visualizations**: Plans for future integration with visual representation tools (e.g., Streamlit).

## Project Structure

- **Book 1** (`01_data_generation_and_analysis.ipynb`): Documenting the mock data generation process and the initial analysis.
- **Book 2** (`02_api_data_integration.ipynb`): Implements the backend system to process the health data (loading, normalizing, and saving the data).

## Step 1: Data Integration

### **Mock Data Generation**
We used [Mockaroo](https://mockaroo.com/) to generate synthetic health data for testing. This data includes various health metrics, such as:
- Daily steps
- Heart rate
- Sleep hours
- Heart rate variability (HRV)
- SPO2 (Oxygen Saturation)

Mock data was saved in a CSV format (`MOCK_DATA.csv`) and serves as the basis for this project.

### **Backend Logic Implementation**
In the second notebook (`02_api_data_integration.ipynb`), the following steps were performed:
1. **Data Loading**: Loaded the generated mock data into a pandas dataframe.
2. **Normalization**: Converted date columns to `datetime` format and ensured consistency in the data.
3. **Data Saving**: Processed data was saved to a new CSV file (`processed_health_data.csv`) for future use.

### **Files in this Repository**
- `MOCK_DATA.csv`: Raw mock health data generated from Mockaroo.
- `processed_health_data.csv`: The normalized and processed data.
- `02_api_data_integration.ipynb`: The notebook where backend logic is implemented (data loading, normalization, and saving).
- `01_data_generation_and_analysis.ipynb`: The notebook showing the data generation process.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/health-tech-dashboard.git

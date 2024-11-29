# Install the required libraries before running:
# pip install pandas streamlit matplotlib plotly

import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
@st.cache
def load_data():
    # Example dataset from Our World in Data (replace with the live dataset if needed)
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    data = pd.read_csv(url)
    return data

# Main function for Streamlit app
def main():
    st.title("COVID-19 Data Dashboard")
    st.write("Visualize COVID-19 data for countries and regions around the world.")
    
    # Load the data
    data = load_data()

    # Sidebar filters
    countries = st.sidebar.multiselect("Select Countries", data["location"].unique(), default=["India", "United States"])
    metric = st.sidebar.selectbox("Select Metric", ["new_cases", "new_deaths", "new_vaccinations"])
    start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
    end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-11-23"))

    # Filter data
    filtered_data = data[
        (data["location"].isin(countries)) &
        (data["date"] >= str(start_date)) &
        (data["date"] <= str(end_date))
    ]

    # Display filtered data
    st.write(f"### COVID-19 {metric.replace('_', ' ').title()} Data")
    st.dataframe(filtered_data[["date", "location", metric]].reset_index(drop=True))

    # Visualization
    st.write("### Visualization")
    fig = px.line(
        filtered_data,
        x="date",
        y=metric,
        color="location",
        title=f"{metric.replace('_', ' ').title()} Over Time",
        labels={"date": "Date", metric: metric.replace('_', ' ').title()},
    )
    st.plotly_chart(fig)

# Run the app
if __name__ == "__main__":
    main()

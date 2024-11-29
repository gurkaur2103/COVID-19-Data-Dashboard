# COVID-19-Data-Dashboard
An interactive Streamlit application for visualizing and analyzing COVID-19 data, using the dataset provided by Our World in Data. This dashboard allows users to explore trends in COVID-19 cases, deaths, and vaccinations over time for selected countries.

# Features
**Data Loading and Filtering**:
=>Retrieves COVID-19 data directly from the Our World in Data repository.
=>Allows filtering by:
   Countries or regions.
   Date range.
   Metrics: New cases, new deaths, or new vaccinations.
  
**Dynamic Visualizations**:
=>Line charts for comparing trends across selected countries.
=>Interactive features using Plotly for better user engagement.

**Data Display**:
=>Shows a preview of filtered data in tabular format.

# Installation
Prerequisites:-
Python 3.7 or higher.
Required libraries: pandas, streamlit, plotly.

# Usage
1.) **Sidebar Options**:
Countries: Select one or more countries for comparison.
Metric: Choose a metric to analyze (new cases, new deaths, or new vaccinations).
Date Range: Adjust the start and end dates to refine your analysis.

2.) **View Data Table**:
Displays the filtered data for selected countries and metric.

3.) **Visualization**:
Interactive line charts showing trends over the specified date range.

# Code Structure
load_data() function:
Caches the dataset for faster loading on repeated use.
Loads data directly from the Our World in Data repository.
# Main Application:
Implements a Streamlit interface with a sidebar for filters.
Generates a table and a line chart based on user inputs.

# Technologies Used
Python: For data processing and backend logic.
Streamlit: To create an interactive web app.
Plotly: For dynamic and visually appealing data visualizations.
Pandas: For efficient data handling and analysis.

# Data Source
This project uses publicly available data from Our World in Data.

# Author
Developed by Gurpreet Kaur.
Feel free to connect on LinkedIn

# Import the libraries
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Charts and Visualizations")

# Data
# Read a csv data, or Excel or maybe generate
@st.cache_data # Cache the data
def generate_data():
    dates = pd.date_range('2025-01-01', periods = 100)
    data = pd.DataFrame({
        'Date' : dates,
        'sales' : np.random.randn(100).cumsum() + 100,
        'profits' : np.random.rand(100).cumsum() + 50,
        'Customers' : np.random.randint(50, 200, 100) 
    })
    return data
data = generate_data()

# Graphs
# Line chart
st.subheader("Line Chart")
st.line_chart(data.set_index('Date')[['sales', 'profits']])

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(data.groupby(data['Date'].dt.month)['sales'].sum())
st.bar_chart(data.set_index('Date')[['sales', 'profits']])

# Area chart
st.subheader("Area Chart")
st.area_chart(data.set_index('Date')[['sales', 'profits']])


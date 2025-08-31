'''
This application will create us an advanced visualization with plotly 
'''
# Import the neccesary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Title
st.title("Advanced Charts with Plotly")

# Sample
df = px.data.gapminder()

# Interactive scatter plot
st.subheader("Interactive Scatter Plot")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig, use_container_width=True)

# 3D plot
st.subheader("3D Plot")
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig_3d = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
st.plotly_chart(fig_3d, use_container_width=True)

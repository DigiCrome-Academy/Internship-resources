import streamlit as st

# st.title("My First Streamlit App")
# st.write("Hello, World. This is my streamlit application. I love Streamlit")

# Title
st.title("Main title")
st.header("Header")
st.subheader("Subheader")

# Text
st.text("This is a plain text")
st.markdown("This is **Bold** and this is *italic*")
st.markdown("### This is a markdown header")

# Code display
st.code("""
def hello():
    print("Hello, streamlit!")
    """, language = 'python')

# laTeX
st.latex(r'''
         e^{i\pi} + 1 = 0
         ''')

# colored text boxes
st.success("THis is a success message!")
st.info("Info Message")
st.warning("Warning Message")
st.error("Error Message!")

import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.jpg")

with col2:
    st.title("Eoin McDonnell")
    content = """
    Hello i am Eoin McDonnell, these are the projects I am working on
    """
    st.info(content)

content2 = """Below you can find the apps that I developed"""

st.info(content2)

col3, col4 = st.columns(2)

#print out the titles from CSV
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

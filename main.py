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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

#print out the titles from CSV
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

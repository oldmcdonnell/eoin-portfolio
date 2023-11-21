import streamlit as st

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

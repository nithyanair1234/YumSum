import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon= "hello",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

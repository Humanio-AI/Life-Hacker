import streamlit as st

st.set_page_config(page_title="Life Hacker Bot", page_icon="🤖", layout="centered")

st.title("🤖 Life Hacker Bot")
st.write("Deployed successfully ✅")

user_q = st.text_input("Ask a question:")
if user_q:
    st.write("You asked:", user_q)

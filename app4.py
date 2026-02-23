import streamlit as st

st.title("simple chatbot")
Question = st.text_input("ask me anything")

if st.button("send"):
    st.write("you asked",Question)
    st.write("chatbot is on the process i will reply soon")
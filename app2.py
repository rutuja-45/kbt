import streamlit as st
st.title("welcome to basic streamlit app")
age=st.slider("select your age",1,100)
city=st.selectbox("select  your city",["Delhi","mumbai","Nashik"])
if st.button("show details"):
    st.write("Age",age)
    st.write("city",city)
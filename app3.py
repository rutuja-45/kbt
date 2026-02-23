import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter your first number")
n1=int(num1)
num2 = st.number_input("Enter your second number")
n2=int(num2)

operation = st.selectbox("Choose operation", ["add", "sub", "mul", "div"])

if st.button("Calculate"):
    if operation == "add":
        st.write("Result:", n1 + n2)

    elif operation == "sub":
        st.write("Result:", n1 - n2)

    elif operation == "mul":
        st.write("Result:", n1 * n2)

    elif operation == "div":
        st.write("Result", n1/n2)

    else:
        st.write("Error: Cannot divide by zero")
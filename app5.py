import streamlit as st

# Custom Button Styling
st.markdown("""
<style>
.stButton > button {
    background-color: green;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Registration Form")

# Create a Form
with st.form("student_form"):
    
    name = st.text_input("Enter your Name")
    age = st.slider("Select your Age", 1, 100)
    city = st.selectbox("Select your City", ["Delhi", "Mumbai", "Nashik"])
    
    submit = st.form_submit_button("Submit")

# After Form Submission
if submit:
    st.success("Form Submitted Successfully!")
    st.write("### 📋 Student Details")
    st.write("**Name:**", name)
    st.write("**Age:**", age)
    st.write("**City:**", city)
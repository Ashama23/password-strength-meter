import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

st.title("Password Strength Meter")
st.markdown("""
Welcome! This app evaluates the strength of your password based on various criteria and 
get suggestions for improvement.
            we will give helpful tips to create a **Strong Password 🔒**.
""")

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0

if password:
    # Check length
    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("❌Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both uppercase and lowercase letters.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character.")
    if score == 4:
        st.success("✅ Your password is strong!")
    elif score == 3:
        st.warning("⚠️ Your password is moderate. Consider adding more complexity.")
    else:
        st.error("❌ Your password is weak. Please improve it based on the feedback below.")

    if feedback:
        st.markdown("## Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to evaluate its strength.")































    #python -m streamlit run password-strenght-meter.py
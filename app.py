import streamlit as st
import pyperclip
from main import generate_email


def format_email(text,Tone,Recepient):
    instruct = f'write/format the email in a {Tone} tone to my {Recepient}'
    prompt = text + "/n" + instruct
    result = generate_email(prompt) #call to the function that will generate result based on prompt
    return result

#page title
st.title("Email Formatter")

# Text input
content_subject = st.text_input("Enter email Subject")
email_content = st.text_area("Enter email content")
content = "Subject: " + content_subject + email_content

# Dropdown menu for Tone Selection
Tones = ["Formal","Friendly","Neutral"]
Tone = st.selectbox("Tones", Tones)

#Dropdown menu for Recepient Designation
Recepient = ["Co-Worker","Boss"]
To = st.selectbox("To", Recepient)

# Button to trigger formatting
if st.button("Format Email"):
    if content:
        formatted_email = format_email(content,Tone,To)
        st.success(formatted_email)

        # Option to copy the output
        if st.button("Copy to Clipboard"):
            pyperclip.copy(formatted_email)
            st.info("Formatted email copied to clipboard.")
    else:
        st.warning("Please enter text before formatting.")



import streamlit as st
import wordle

# Title for the app
st.title("Wordle Helper")

# Input text form
user_input = st.text_input("")

# Get Wordle helper results
args = user_input.split()
results = wordle.main(args)

# Output text box
if user_input:
    st.text(results)

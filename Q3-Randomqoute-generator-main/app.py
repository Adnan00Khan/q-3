import os
import streamlit as st
import random

st.title("Random Quote Generator")

def get_random_quote():
    current_dir = os.getcwd()  # Get current working directory
    st.write(f"Current directory: {current_dir}")  # Display the current directory on the app

    try:
        with open("q 3\Q3-Randomqoute-generator-main\quotes.txt", "r", encoding="utf-8") as file:
            quotes = file.readlines()
        return random.choice(quotes).strip()
    except FileNotFoundError:
        return "Error: quotes.txt file not found!"

if st.button("Generate Quote"):
    st.success(get_random_quote())

import streamlit as st
import random

st.title("Random Quote Generator")

def get_random_quote():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

if st.button("Generate Quote"):
    st.success(get_random_quote())

# Add watermark-style text
st.markdown("<br><br><hr style='border:1px solid gray'><p style='text-align:center; font-size:12px; color:gray;'>Created by AK SoftTech</p>", unsafe_allow_html=True)
import streamlit as st;

st.set_page_config(page_title = "My webPage" , page_icon= ":tada:", layout= "wide");

# Header
st.title("Welcome to AK Quotes Collection");
st.subheader("A page full of mind blowing motivations");
st.write("One thought can change your day—let it be an inspiring one!")

#section
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with  left_column:
        st.subheader("Elevate Your Mind, Ignite Your Potential!")
        st.write("A space where motivation meets action, pushing you towards your dreams with unstoppable energy.")
        st.write("######")
        st.write(""" Welcome to a page full of mind-blowing motivations—where 
        inspiration meets action! 🌟 Life is a journey filled with challenges,
        but the right mindset can turn obstacles into stepping stones. Here,
        every word is designed to uplift, empower, and ignite your inner drive.
        Whether you're chasing dreams, overcoming doubts, or seeking a spark of encouragement,
        this space is your daily dose of positivity. Let these words fuel your 
        ambition, push your limits, and remind you that greatness lies within you.
        Believe in yourself, embrace the journey, and watch how motivation transforms into
        unstoppable success! 🚀✨ """)
        st.write("[learn more] (https://www.youtube.com/@Buggs_____________bunnyyy)")
        st.write("[Instagram] (https://www.instagram.com/bugs____bunnyyyy__/#)")
        st.write("####")
        st.text("""Thank you for visiting the site! 🌟 May you leave with a heart 
        full of inspiration and a mind ready to conquer new heights. Keep striving,
        keep shining, and remember—greatness begins with a single step! 🚀✨""")
        
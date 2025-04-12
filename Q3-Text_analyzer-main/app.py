import streamlit as st

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="centered")
    
    # Custom Styling
    st.markdown(
        """
        <style>
            .stTextArea, .stTextInput {border-radius: 10px; padding: 5px;}
            .stButton>button {background-color: #4CAF50; color: white; border-radius: 5px;}
            .stMarkdown {font-size: 18px; color: #333366;}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""<h1 style='text-align: center; color: #4CAF50;'>Text Analyzer</h1>""", unsafe_allow_html=True)
    
    # User input
    paragraph = st.text_area("Enter a paragraph:", key="input_text")
    
    if paragraph.strip():
        # Word and Character Count
        word_count = len(paragraph.split())
        char_count = len(paragraph)
        
        # Vowel Count
        vowel_count = count_vowels(paragraph)
        
        # Search and Replace
        search_word = st.text_input("Enter a word to search:")
        replace_word = st.text_input("Enter a word to replace it with:")
        
        modified_text = paragraph.replace(search_word, replace_word) if search_word else paragraph
        
        # Uppercase and Lowercase Conversion
        uppercase_text = paragraph.upper()
        lowercase_text = paragraph.lower()
        
        # Type Casting
        word_count_str = str(word_count)
        vowel_count_str = str(vowel_count)
        
        # Operators
        contains_python = "✅ Yes" if "Python" in paragraph else "❌ No"
        avg_word_length = char_count / word_count if word_count > 0 else 0
        
        # Display results
        st.markdown("""<h2 style='color: #FF5733;'>Analysis Results:</h2>""", unsafe_allow_html=True)
        st.success(f"**Total Words:** {word_count_str}")
        st.info(f"**Total Characters (including spaces):** {char_count}")
        st.warning(f"**Total Vowels:** {vowel_count_str}")
        st.error(f"**Contains 'Python':** {contains_python}")
        st.markdown(f"**Average Word Length:** `{avg_word_length:.2f}`")
        
        st.markdown("""<h2 style='color: #007BFF;'>Modified Text:</h2>""", unsafe_allow_html=True)
        st.text_area("Modified Paragraph:", modified_text, height=150)
        
        st.markdown("""<h2 style='color: #9C27B0;'>Uppercase Text:</h2>""", unsafe_allow_html=True)
        st.text_area("Uppercase Version:", uppercase_text, height=100)
        
        st.markdown("""<h2 style='color: #009688;'>Lowercase Text:</h2>""", unsafe_allow_html=True)
        st.text_area("Lowercase Version:", lowercase_text, height=100)
    else:
        st.warning("⚠ Please enter a paragraph to analyze.")
    
    st.markdown("""<p style='text-align: center; font-weight: bold; color: #555;'>Created By Adnan Khan</p>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
import streamlit as st
from transformers import pipeline

# Cache the model loading to speed up app reloads
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Streamlit UI
st.title("Text Summarization App")

text_input = st.text_area("Enter the text you want to summarize:")

if st.button("Summarize"):
    if text_input and len(text_input.split()) > 30:
        with st.spinner("Generating summary..."):
            summary = summarizer(text_input, max_length=150, min_length=50, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    elif text_input:
        st.warning("Please enter at least 30 words for better summarization results!")
    else:
        st.warning("Please enter some text first!")

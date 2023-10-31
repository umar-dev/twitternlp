import streamlit as st
import requests

# Define the API URL and API key
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer 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"}

# Define the sentiment analysis function
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        sentiment_label = result[0]["label"]
        sentiment_score = result[0]["score"]
        return sentiment_label, sentiment_score
    else:
        return None

# Streamlit app
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter a text:")

if st.button("Analyze Sentiment"):
    if user_input:
        sentiment_label, sentiment_score = query({"inputs": user_input})
        st.write(f"Sentiment: {sentiment_label}")
        st.write(f"Score: {sentiment_score}")

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
        return result
    else:
        return None

# Streamlit app
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter a text:")

if st.button("Analyze Sentiment"):
    if user_input:
        result = query({"inputs": user_input})
        if result:
            # Display the JSON response as a table
            st.table(result)
        else:
            st.error("Error in API response. Please check your input or try again.")

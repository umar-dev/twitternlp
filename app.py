import streamlit as st

# Define the API call function
def query(payload):
    # Your query function code here...

# Streamlit app
st.title("Sentiment Analysis App")
user_input = st.text_area("Enter a text:")
if st.button("Analyze Sentiment"):
    if user_input:
        sentiment_label, sentiment_score = query({"inputs": user_input})
        st.write(f"Sentiment: {sentiment_label}")
        st.write(f"Score: {sentiment_score}")

import streamlit as st
import requests

st.title("📰 News Summarization & Sentiment Analysis")

# Store company name input in session state
if "company_name" not in st.session_state:
    st.session_state.company_name = ""

st.session_state.company_name = st.text_input("Enter Company Name", st.session_state.company_name)

# Store articles in session state
if "articles" not in st.session_state:
    st.session_state.articles = []

if st.button("Get News"):
    response = requests.get(f"http://127.0.0.1:5000/get_news?company={st.session_state.company_name}")
    
    if response.status_code == 200:
        data = response.json()
        st.session_state.articles = data["articles"]  # Save articles in session state

# Display stored news articles
if st.session_state.articles:
    st.write(f"## News Articles for {st.session_state.company_name}")

    for index, article in enumerate(st.session_state.articles):
        st.subheader(article["title"])
        st.write("**Summary:**", article["summary"])
        st.write("**Sentiment:**", article["sentiment"]["label"])

        if st.button(f"🔊 Generate Hindi Audio for {article['title']}", key=f"tts_{index}"):
            audio_response = requests.post("http://127.0.0.1:5000/generate_audio", json={"text": article["summary"]})
            if audio_response.status_code == 200:
                st.audio("output.mp3", format="audio/mp3")
            else:
                st.error("Failed to generate audio.")



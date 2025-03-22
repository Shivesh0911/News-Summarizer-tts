Here’s your properly formatted `README.md` in one go:  

```md
# News Summarization and Text-to-Speech Application

## Overview
This is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool allows users to input a company name and receive a structured sentiment report along with an audio output.

---

## Features
- **News Extraction**: Fetches news articles related to a given company using the GNews API.
- **Text Summarization**: Summarizes the content of each article using the `distilbart-cnn-12-6` model.
- **Sentiment Analysis**: Analyzes the sentiment of each article (positive, negative, or neutral) using a pre-trained sentiment analysis model.
- **Text-to-Speech (TTS)**: Converts the summarized content into Hindi speech using `gTTS`.
- **Web Interface**: Provides a simple and intuitive user interface using Streamlit.
- **API Integration**: The frontend communicates with the backend via Flask APIs.

---

## Project Structure
```
news-summarization-app/
├── api.py                 # Flask backend for API endpoints
├── app.py                 # Streamlit frontend for user interaction
├── news_scraper.py        # Fetches news articles using GNews API
├── sentiment_analysis.py  # Performs sentiment analysis on article summaries
├── text_summarizer.py     # Summarizes article content
├── tts_generator.py       # Generates Hindi TTS from summarized text
├── requirements.txt       # Lists all dependencies
└── README.md              # Project documentation
```

---

## Dependencies
The project uses the following Python libraries:
- **Flask**: For creating the backend API.
- **Streamlit**: For the frontend web interface.
- **Requests**: For making HTTP requests to the GNews API.
- **Transformers**: For sentiment analysis and text summarization.
- **gTTS**: For generating Hindi text-to-speech.
- **googletrans**: For translating English text to Hindi.
- **Torch**: Required by the `transformers` library for running models.

All dependencies are listed in the `requirements.txt` file.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd news-summarization-app
```

### 2. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Set Up GNews API Key
Replace the placeholder API key in `news_scraper.py` with your actual GNews API key:
```python
API_KEY = "your_gnews_api_key_here"
```

### 4. Run the Backend (Flask API)
Start the Flask server:
```bash
python api.py
```
The backend will run on `http://127.0.0.1:5000`.

### 5. Run the Frontend (Streamlit App)
Start the Streamlit app:
```bash
streamlit run app.py
```
The frontend will open in your browser at `http://localhost:8501`.

---

## Usage

1. Open the Streamlit app in your browser.
2. Enter the name of a company (e.g., "Tesla") in the input field.
3. Click **"Get News"** to fetch and display news articles.
4. View the title, summary, and sentiment of each article.
5. Click **"Generate Hindi Audio"** to listen to the summarized content in Hindi.

---

## API Endpoints

### 1. Fetch News Articles
- **Endpoint**: `/get_news`
- **Method**: `GET`
- **Parameters**:
  - `company`: Name of the company (e.g., Tesla).
- **Response**:
  ```json
  {
    "company": "Tesla",
    "articles": [
      {
        "title": "Tesla's New Model Breaks Sales Records",
        "summary": "Tesla's latest EV sees record sales in Q3...",
        "sentiment": {"label": "Positive", "score": 0.95}
      }
    ]
  }
  ```

### 2. Generate Hindi TTS
- **Endpoint**: `/generate_audio`
- **Method**: `POST`
- **Parameters**:
  - `text`: Text to be converted to Hindi speech.
- **Response**:
  ```json
  {
    "audio_file": "output.mp3"
  }
  ```

---

## Deployment on Hugging Face Spaces

1. Create a new **Space** on Hugging Face.
2. Upload all project files (`api.py`, `app.py`, etc.) to the Space.
3. Add the `requirements.txt` file to install dependencies.
4. Configure the Space to run the Streamlit app:
   - Set the **Space SDK** to **Streamlit**.
   - Add the following command to the **README.md** of the Space:
     ```bash
     streamlit run app.py
     ```
5. Deploy the Space and test the application.

---

## Assumptions and Limitations

- **News Source**: The application relies on the GNews API for fetching news articles. Ensure you have a valid API key.
- **Translation Accuracy**: The translation from English to Hindi is done using `googletrans`, which may not always be 100% accurate.
- **TTS Quality**: The quality of the Hindi TTS depends on the `gTTS` library and may vary for complex sentences.
- **Scalability**: The application is designed for small-scale use. For large-scale deployments, consider optimizing the backend and using a more robust translation service.

---

## Future Enhancements

- **Advanced Sentiment Analysis**: Use domain-specific sentiment analysis models for better accuracy.
- **Multi-language Support**: Extend the TTS functionality to support multiple languages.
- **Caching**: Implement caching for news articles to reduce API calls.
- **Error Handling**: Improve error handling for edge cases (e.g., no news found for a company).

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: [shivesh0911@gmail.com](mailto:shivesh0911@gmail.com)
- **GitHub**: [https://github.com/Shivesh0911](https://github.com/Shivesh0911)
```

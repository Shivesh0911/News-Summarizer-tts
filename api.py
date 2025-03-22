from flask import Flask, request, jsonify
from news_scraper import fetch_news
from text_summarizer import summarize_text
from sentiment_analysis import analyze_sentiment
from tts_generator import generate_hindi_tts

app = Flask(__name__)

@app.route("/get_news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    articles = fetch_news(company)
    
    for article in articles:
        article["summary"] = summarize_text(article["title"])
        article["sentiment"] = analyze_sentiment(article["summary"])
    
    return jsonify({"company": company, "articles": articles})

@app.route("/generate_audio", methods=["POST"])
def generate_audio():
    data = request.json
    text = data.get("text")
    filename = generate_hindi_tts(text, filename="output.mp3")  # Change to .mp3
    if filename:
        return jsonify({"audio_file": filename})
    else:
        return jsonify({"error": "Failed to generate audio"}), 500

if __name__ == "__main__":
    app.run(debug=True)

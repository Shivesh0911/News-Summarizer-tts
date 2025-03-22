from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")


def summarize_text(text):
    input_length = len(text.split())  # Count words in input text
    max_len = min(100, input_length)  # Set max_length dynamically
    min_len = min(30, input_length // 2)  # Ensure min_length is reasonable
    
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]["summary_text"]

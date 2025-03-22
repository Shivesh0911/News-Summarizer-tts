import requests

API_KEY = "f4cb93998bb41b7a6530bfa774b2d956"  # Replace with your actual GNews API key

def fetch_news(company_name):
    url = f"https://gnews.io/api/v4/search?q={company_name}&token={API_KEY}&lang=en"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching news:", response.status_code, response.text)
        return []

    data = response.json()
    articles = [{"title": article["title"], "url": article["url"]} for article in data.get("articles", [])]
    
    print("Extracted Articles:", articles)  # Debugging
    return articles

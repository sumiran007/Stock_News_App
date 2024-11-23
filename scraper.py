import requests
import csv
import time
import signal
import sys
from datetime import datetime, timedelta

# Number of days to go back for fetching news
age = 30

# List of keywords to ensure relevance
keywords = ['NVIDIA', 'GeForce', 'RTX', 'GPU', 'graphics card', 'AI', 'artificial intelligence']

# Function to fetch news data
def fetch_data():
    language = 'en'
    api_key = '2b10aec4297f49439dd0d061cb84e7f4'
    query = 'NVIDIA'
    from_date = (datetime.now() - timedelta(days=age)).strftime('%Y-%m-%d')  # Fetch news from the past 'age' days
    url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={api_key}&language={language}'
    response = requests.get(url)
    data = response.json()
    return data

# Function to check if an article is relevant based on keywords
def is_relevant(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    for word in keywords:
        if word.lower() in title or word.lower() in description:
            return True
    return False

# Function to load processed URLs from CSV file
def load_processed_urls(filename):
    processed_urls = set()
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    processed_urls.add(row[1].strip())
    except FileNotFoundError:
        pass
    return processed_urls

# Function to parse and save relevant articles to CSV file
def parse_and_save_data(data, processed_urls, filename):
    articles = data.get('articles', [])
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for article in articles:
            url = article.get('url', '').strip()
            headline = article.get('title', '').strip()
            published_date = article.get('publishedAt', '').strip()
            if is_relevant(article) and url not in processed_urls:
                print(f"Headline: {headline}")
                print(f"URL: {url}")
                print(f"Published Date: {published_date}\n")
                writer.writerow([headline, url, published_date])
                processed_urls.add(url)

# Function to handle exit event
def handle_exit(signum, frame):
    print("Bye")
    sys.exit(0)

# Register the exit event handler
signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# Main loop to keep the script running
filename = 'nvidia_news.csv'
processed_urls = load_processed_urls(filename)

while True:
    try:
        data = fetch_data()
        parse_and_save_data(data, processed_urls, filename)
    except Exception as e:
        print(f"Something is Wrong: {e}")
    
    
    exit()
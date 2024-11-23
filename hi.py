import requests
import csv
import time
import signal
import sys
from datetime import datetime, timedelta

# Function to fetch news data
def fetch_data():
    apikey = '2b10aec4297f49439dd0d061cb84e7f4'
    query = 'NVIDIA'
    fromd = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    url = f'https://newsapi.org/v2/everything?q={query}&from={fromd}&sortBy=publishedAt&apiKey={apikey}'
    response = requests.get(url)
    data = response.json()
    return data

def load_processed_urls(filename):
    processed_urls = set()
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    processed_urls.add(row[0].strip())
    except FileNotFoundError:
        pass
    return processed_urls


def parse_and_save_data(data, processed_urls, filename):
    if 'articles' not in data:
        print("Error: 'articles' key not found in the response.")
        print("Response data:", data)
        return

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for article in data['articles']:
            headline = article['title']
            url = article['url']
            published_date = article['publishedAt']
            
            if url not in processed_urls:
                print(f"Headline: {headline}")
                print(f"URL: {url}")
                print(f"Published Date: {published_date}\n")
                writer.writerow([headline])
                writer.writerow([url])
                writer.writerow([published_date])
                writer.writerow([])  
                processed_urls.add(url)


def handle_exit(signum, frame):
    print("Bye")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)


filename    = 'nvidia_news.csv'
processed_urls = load_processed_urls(filename)

while True:
    try:
        data = fetch_data()
        parse_and_save_data(data, processed_urls, filename)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    time.sleep(60)  # Wait for 60 seconds before fetching data again

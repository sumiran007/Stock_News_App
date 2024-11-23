import plotly.graph_objects as go
import time
from datetime import datetime
import requests

API_KEY = 'sQFTHosaQwg_zF7t1cAiMerxpeNswGkx'  # Replace with your Polygon API key

def fetch_data():
    url = f'https://api.polygon.io/v2/aggs/ticker/NVDA/range/1/day/2023-01-09/2024-02-10?adjusted=true&sort=asc&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def parse_data(data):
    results = data.get('results', [])
    x = [datetime.fromtimestamp(item['t'] / 1000) for item in results]
    y = [item['c'] for item in results]
    return x, y

# Create a combined figure
fig = go.Figure()

# Add stock data trace
data = fetch_data()
x_stock, y_stock = parse_data(data)
fig.add_trace(go.Scatter(x=x_stock, y=y_stock, mode='lines', name='NVDA Stock Prices'))

# Update layout
fig.update_layout(
    title='NVDA Stock Prices Over Time',
    xaxis_title='Date',
    yaxis_title='Close Price/$'
)

# Show the plot
fig.show()

# Update the plot in a loop
while True:
    data = fetch_data()
    x_stock, y_stock = parse_data(data)
    fig.update_traces(x=x_stock, y=y_stock)
    fig.show()
    time.sleep(60)
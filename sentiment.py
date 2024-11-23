from transformers import pipeline
import pandas as pd
import torch
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="torchvision")
# Check if a GPU is available and set the device accordingly
use_gpu = torch.cuda.is_available()

# Create a sentiment analysis pipeline with GPU support if available
sentiment_analysis = pipeline('sentiment-analysis', device=0 if use_gpu else -1)

# Load the data
df = pd.read_csv('nvidia_news_formatted.csv')

# Print the column names to check what they are
print(df.columns)

# Apply sentiment analysis to every headline if the column exists
if 'headline' in df.columns:
    df['Sentiment'] = df['headline'].apply(lambda x: sentiment_analysis(x)[0]['label'])
elif 'Headline' in df.columns:
    df['Sentiment'] = df['Headline'].apply(lambda x: sentiment_analysis(x)[0]['label'])
else:
    print("Column 'headline' or 'Headline' not found in the DataFrame")

# Save the results to a new CSV file if the sentiment analysis was applied
if 'Sentiment' in df.columns:
    df.to_csv('nvidia_news_sentiment.csv', index=False)

print("Sentiment analysis completed and saved to 'nvidia_news_sentiment.csv'")
exit(0)
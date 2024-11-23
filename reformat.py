import csv

# Read the existing CSV file
with open('nvidia_news.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    lines = list(reader)

# Process the data to extract headline, link, and date
data = []
for row in lines:
    if len(row) == 3:  # Ensure there are exactly 3 columns
        headline = row[0].strip()
        link = row[1].strip()
        date = row[2].strip()
        data.append([headline, link, date])

# Save the processed data to a new CSV file
with open('nvidia_news_formatted.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(['headline', 'link', 'date'])  # Write the header
    writer.writerows(data)

print("Formatted CSV file saved as 'nvidia_news_formatted.csv'")
exit(0)
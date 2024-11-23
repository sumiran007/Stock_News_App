import subprocess

# Run scraper.py
print("Running scraper.py...")
subprocess.run(["python", "scraper.py"], check=True)
print("scraper.py completed.")

# Run reformat.py
print("Running reformat.py...")
subprocess.run(["python", "reformat.py"], check=True)
print("reformat.py completed.")

# Run sentiment.py
print("Running sentiment.py...")
subprocess.run(["python", "sentiment.py"], check=True)
print("sentiment.py completed.")

print("All scripts have been run successfully.")
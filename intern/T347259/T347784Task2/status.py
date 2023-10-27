import csv
import requests

# Function to get status code or "Error" for a URL
def get_status_code(url):
    try:
        response = requests.head(url)
        return response.status_code
    except requests.exceptions.RequestException:
        return "Error"

# Input CSV file name
csv_file = "Task 2 -Intern.csv"

# Read URLs from the CSV file
with open(csv_file, "r") as input_file:
    csv_reader = csv.reader(input_file)
    next(csv_reader)  # Skip the header row
    urls = [row[0] for row in csv_reader]

# Process the URLs and print the results
for url in urls:
    status = get_status_code(url)
    print(f"({status}) {url}")

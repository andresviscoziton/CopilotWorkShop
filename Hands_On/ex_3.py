import requests
from bs4 import BeautifulSoup
import csv

# Function to send a GET request to a news website URL
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Function to parse HTML and extract news article titles
def extract_titles(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        titles = [title.get_text() for title in soup.find_all('h2')]
        return titles
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return []

# Function to save titles to a CSV file
def save_to_csv(titles, filename):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title"])
            for title in titles:
                writer.writerow([title])
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Main function to scrape data and save to CSV
def main():
    url = "https://www.infobae.com/"
    html = fetch_html(url)
    if html:
        titles = extract_titles(html)
        if titles:
            save_to_csv(titles, "news_titles.csv")
            print("Titles saved to news_titles.csv")
        else:
            print("No titles found.")
    else:
        print("Failed to retrieve HTML.")

if __name__ == "__main__":
    main()
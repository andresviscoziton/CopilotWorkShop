# import requests
# from bs4 import BeautifulSoup
# import csv


# def fetch_html(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return response.text
#     except requests.RequestException as e:
#         print(f"Error fetching the URL: {e}")
#         return None

# def parse_titles(html):
#     try:
#         soup = BeautifulSoup(html, 'html.parser')
#         titles = [title.get_text() for title in soup.find_all('h2')]
#         return titles
#     except Exception as e:
#         print(f"Error parsing HTML: {e}")
#         return []

# def save_to_csv(titles, filename):
#     try:
#         with open(filename, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["Title"])
#             for title in titles:
#                 writer.writerow([title])
#     except Exception as e:
#         print(f"Error saving to CSV: {e}")

# def main():
#     url = "https://www.infobae.com/"
#     html = fetch_html(url)
#     if html:
#         titles = parse_titles(html)
#         if titles:
#             save_to_csv(titles, "news_titles.csv")
#             print("Titles saved to news_titles.csv")
#         else:
#             print("No titles found.")
#     else:
#         print("Failed to retrieve HTML.")

# if __name__ == "__main__":
#     main()
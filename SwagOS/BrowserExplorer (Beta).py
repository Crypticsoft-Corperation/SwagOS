import urllib.request
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    except urllib.error.URLError as e:
        print(f"Error fetching the webpage: {e}")
        return None

def display_links(soup):
    if soup:
        print("Links on the page:")
        links = soup.find_all('a')
        for index, link in enumerate(links, start=1):
            href = link.get('href')
            text = link.text.strip()
            print(f"{index}. {text} - {href}")
    else:
        print("No webpage content to display.")

if __name__ == "__main__":
    print("Browser Explorer 1.0")
    while True:
        user_input = input("Enter a URL (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        webpage = fetch_webpage(user_input)
        display_links(webpage)

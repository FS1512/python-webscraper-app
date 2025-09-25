import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    try: 
        response = requests.get(url, timeout=10)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = []
        for tag in soup.find_all(['h2', 'h3']):
            title = tag.get_text(strip=True)
            if title:
                headlines.append(title)

            
            with open('headlines.txt', 'w') as file:
                for i, headline in enumerate(headlines):
                    file.write(f"{i+1}. {headline}\n")

            print(f"{len(headlines)} headlines scraped from '{url}'.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the news website(or press enter for BBC): ")
    if not url:
        url = "https://www.bbc.com/news"
    scrape_headlines(url)
import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    """
    Scrapes the top headlines from the BBC News homepage.
    """
    URL = "https://www.bbc.com/news"
    
    print(f"📰 Scraping top headlines from {URL}...")

    try:
        # --- Make the HTTP request ---
        response = requests.get(URL, timeout=10)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # --- Parse the HTML ---
        soup = BeautifulSoup(response.content, 'html.parser')

        # --- Find all headline elements ---
        # The specific tag and class name can change if BBC updates their website.
        # As of late 2025, 'h2' elements with a specific data-testid attribute are used for main headlines.
        headlines = soup.find_all('h2', {'data-testid': 'card-headline'})
        
        if not headlines:
            print("Could not find headlines. The website's structure may have changed.")
            return

        print("\n--- Top Headlines ---")
        for i, headline in enumerate(headlines[:10]): # Get the first 10 headlines
            print(f"{i+1}. {headline.get_text().strip()}")
        print("---------------------\n")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error fetching the URL: {e}")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    scrape_bbc_news()

import requests

def shorten_url(long_url):
    """
    Uses the TinyURL API to shorten a given long URL.
    
    :param long_url: The original, long URL string.
    :return: The shortened URL string or an error message.
    """
    # The API endpoint for TinyURL does not require an API key
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    
    try:
        response = requests.get(api_url)
        # The API returns the shortened URL in plain text
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to the API. {e}"

# --- Main execution block ---
if __name__ == "__main__":
    print("🔗 Simple URL Shortener 🔗")
    original_url = input("Enter the long URL to shorten: ")

    # Basic check to ensure the input looks like a URL
    if not original_url.startswith(('http://', 'https://')):
        print("Invalid input. Please enter a full URL (e.g., https://www.google.com).")
    else:
        short_url = shorten_url(original_url)
        print("\n---------------------------------")
        print(f"Shortened URL: {short_url}")
        print("---------------------------------")

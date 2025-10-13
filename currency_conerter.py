import requests

def convert_currency():
    """
    Converts an amount from one currency to another using the Frankfurter API.
    """
    print("💹 Real-Time Currency Converter 💹")
    
    # --- Get User Input ---
    amount = input("Enter the amount to convert: ")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., INR): ").upper()

    # --- Construct the API URL ---
    # Using the free and open-source Frankfurter API (no API key required)
    api_url = f"https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={target_currency}"

    try:
        print("\nFetching latest exchange rates...")
        response = requests.get(api_url)
        # Raise an exception for bad status codes (like 404 or 500)
        response.raise_for_status() 
        
        data = response.json()
        
        # --- Extract and Display the Result ---
        if 'rates' in data and target_currency in data['rates']:
            converted_amount = data['rates'][target_currency]
            print("\n" + "="*40)
            print(f"  {amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
            print("="*40)
        else:
            print("Could not find the exchange rate. Please check the currency codes.")

    except requests.exceptions.HTTPError as err:
        print(f"❌ HTTP Error: Could not process the request. The API may be down or the currency code is invalid.")
        print(f"   Details: {err}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error: Could not connect to the API. Please check your internet connection.")
        print(f"   Details: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    convert_currency()

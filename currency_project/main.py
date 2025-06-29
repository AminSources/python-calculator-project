import requests


def get_currency_data():
    api_key = "insert_your_api_key_here"

    try:
        # Fetch the latest currency data from the API
        response = requests.get(
            "https://api.freecurrencyapi.com/v1/latest", params={"apikey": api_key}
        )

        # Check if the API request was successful
        if response.status_code == 200:
            return response.json().get("data", {})
        else:
            print(f"Error: {response.status_code}")
            return {}

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {}


currency_data = get_currency_data()

# Print the fetched currency codes and prices
if currency_data:
    print("Currency Codes and Prices:")
    for code, price in currency_data.items():
        print(f"{code}: {price:.2f} USD")
else:
    print("No currency data found.")

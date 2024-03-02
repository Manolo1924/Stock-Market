import requests

ALPHA_VANTAGE_API_KEY = 'YOUR API KEY'
BASE_URL = 'https://www.alphavantage.co/query'
FUNCTION = 'GLOBAL_QUOTE'

def get_stock_price(symbol):
    try:
        params = {
            'function': FUNCTION,
            'symbol': symbol,
            'apikey': ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if 'Global Quote' in data:
            stock_data = data['Global Quote']
            price = stock_data.get('05. price')
            return price
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Alpha Vantage: {e}")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    print("Welcome to the Stock Market Search Tool!")

    while True:
        search_symbol = input("Enter the stock symbol to search (type 'exit' to quit): ")

        if search_symbol.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            price = get_stock_price(search_symbol)

            if price:
                print(f"Current price of {search_symbol.upper()}: {price}")
            else:
                print(f"Failed to retrieve data for {search_symbol.upper()}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

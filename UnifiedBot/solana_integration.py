import requests

# Define the Solana Serum DEX API URL
SOLANA_SERUM_API_URL = "https://serum-api.bonfida.com/orderbooks/"

def fetch_solana_token_price(token_symbol):
    """
    Fetch the price of a token from Solana's Serum DEX.
    :param token_symbol: The symbol of the token (e.g., 'SOL', 'USDC')
    :return: The price of the token
    """
    api_url = f"{SOLANA_SERUM_API_URL}{token_symbol}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise error for bad status codes

        price_data = response.json()
        best_ask = price_data['data']['asks'][0][0]  # Get the best ask price

        return best_ask
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data for {token_symbol}: {e}")
        return None

# Example usage
sol_price = fetch_solana_token_price("SOLUSDT")
usdc_price = fetch_solana_token_price("USDCUSDT")

print(f"SOL Price (in USDT): {sol_price}")
print(f"USDC Price (in USDT): {usdc_price}")

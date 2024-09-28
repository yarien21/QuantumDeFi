import requests

COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price'

def fetch_solana_token_price(token_ids):
    """
    Fetch the price of a token using CoinGecko API.
    :param token_ids: The ID of the token(s) (e.g., 'solana', 'usd-coin')
    :return: The price of the token in USDT or an error if not supported
    """
    params = {
        'ids': token_ids,  # Token IDs in CoinGecko format
        'vs_currencies': 'usd'  # Convert to USD
    }

    try:
        response = requests.get(COINGECKO_API_URL, params=params)
        response.raise_for_status()

        price_data = response.json()
        return price_data[token_ids]['usd']  # Extract USD price
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data for {token_ids}: {e}")
        return None

# Example usage
sol_price = fetch_solana_token_price("solana")
usdc_price = fetch_solana_token_price("usd-coin")

print(f"SOL Price (in USDT): {sol_price}")
print(f"USDC Price (in USDT): {usdc_price}")

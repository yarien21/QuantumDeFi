import requests

class APIError(Exception):
    pass

def fetch_token_price(token_address, chain="ethereum"):
    # Choose API URL for Matcha (0x API)
    api_url = "https://api.0x.org/swap/v1/price"

    # Define query parameters for Matcha (0x API)
    params = {
        'sellToken': token_address,  # The token you're selling (ERC20 for Ethereum)
        'buyToken': '0xdAC17F958D2ee523a2206206994597C13D831ec7',  # USDT contract address
        'sellAmount': 1000000000000000000,  # 1 token in wei (1 ETH in wei)
        'slippagePercentage': 0.01,  # 1% slippage tolerance
        'network': 1 if chain == "ethereum" else 137  # 1 for Ethereum, 137 for Polygon (Matcha supports Polygon)
    }

    try:
        # Send the request
        print(f"Calling API URL: {api_url} with params: {params}")
        response = requests.get(api_url, params=params)
        print(f"API Response Status Code: {response.status_code}")
        print(f"API Raw Response: {response.text}")

        # Ensure response is valid JSON and status code is 200
        if response.status_code != 200:
            raise APIError(f"API returned an error: {response.status_code} - {response.text}")

        # Parse the JSON data
        price_data = response.json()

        # Display the result
        print(f"Parsed Response: {price_data}")
        return price_data.get('price')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data: {e}")
    except APIError as e:
        print(f"API Error: {e}")

# Example token addresses
weth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"  # WETH on Ethereum
matic_address = "0x0000000000000000000000000000000000001010"  # MATIC on Polygon (no WBNB)

# Example usage
eth_price = fetch_token_price(weth_address, chain="ethereum")
matic_price = fetch_token_price(matic_address, chain="polygon")

print(f"WETH Price (Ethereum in USDT): {eth_price}")
print(f"MATIC Price (Polygon in USDT): {matic_price}")

#
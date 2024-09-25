import requests

class APIError(Exception):
    pass

def fetch_token_price(token_address, chain="ethereum"):
    # Choose API URL based on the chain
    if chain == "ethereum":
        api_url = f"https://api.1inch.io/v5.0/1/swap"
    elif chain == "bsc":
        api_url = f"https://api.1inch.io/v5.0/56/swap"
    else:
        raise ValueError("Unsupported chain")

    # Define query parameters
    params = {
        'fromTokenAddress': token_address,  # The token address (ERC20 for Ethereum, BEP20 for BSC)
        'toTokenAddress': '0xdAC17F958D2ee523a2206206994597C13D831ec7',  # USDT contract address
        'amount': 1000000000000000000,  # 1 token in wei (1 ETH in wei)
        'fromAddress': '0x0000000000000000000000000000000000000000',  # Dummy address, required for API
        'slippage': 1,  # 1% slippage tolerance
        'disableEstimate': 'true'  # Disable gas estimation (to get quote faster)
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
        return price_data.get('toTokenAmount')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data: {e}")
    except APIError as e:
        print(f"API Error: {e}")

# Example token addresses
weth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"  # WETH on Ethereum
wbnb_address = "0xBB4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"  # WBNB on BSC

# Example usage
eth_price = fetch_token_price(weth_address, chain="ethereum")
bnb_price = fetch_token_price(wbnb_address, chain="bsc")

print(f"WETH Price (Ethereum in USDT): {eth_price}")
print(f"WBNB Price (BSC in USDT): {bnb_price}")

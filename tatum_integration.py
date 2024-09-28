import requests
import json

# Define the base URL for the Tatum API and headers for authentication
BASE_URL = "https://api.tatum.io/v3"

# Replace with your valid Tatum API key
TATUM_API_KEY = "t-66f6471c6be651758a55d0d3-2cde95375c824b0d8a8bd491"

# Define the headers for making API calls to Tatum
HEADERS = {
    'x-api-key': TATUM_API_KEY,
    'Content-Type': 'application/json',
    'accept': 'application/json'
}

# Centralized function for making API calls
def make_api_call(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API call to {url}: {e}")
        return None

# Function to generate a new Ethereum wallet using Tatum API
def generate_wallet(currency="ethereum"):
    endpoint = f"{currency}/wallet"
    print(f"Generating {currency.upper()} wallet...")
    return make_api_call(endpoint)

# Function to derive a new Ethereum address from an xpub
def derive_eth_address(xpub, index=0):
    endpoint = f"ethereum/address/{xpub}/{index}"
    print(f"Deriving Ethereum address from xpub at index {index}...")
    response = make_api_call(endpoint)
    return response.get('address') if response else None

# Function to get the balance of an Ethereum address using Tatum API
def get_balance(currency, address):
    """
    Fetch the balance of a given Ethereum address.
    Updated to use the account-specific balance endpoint.
    """
    # Switching to the account balance endpoint instead
    endpoint = f"{currency}/account/balance/{address}"
    print(f"Fetching balance for {currency.upper()} address: {address}...")
    response = make_api_call(endpoint)
    return response if response else None

# Function to get the balance of a token (e.g., USDT) using Tatum API
def get_token_balance(address, contract_address):
    """
    Fetch the balance of an ERC-20 token using the correct endpoint.

    :param address: Ethereum address to check.
    :param contract_address: Contract address of the ERC-20 token.
    :return: Balance of the specified ERC-20 token.
    """
    # Use Tatum's correct ERC-20 token balance endpoint
    endpoint = f"ethereum/account/balance/{address}?contractAddress={contract_address}"
    print(f"Fetching ERC-20 Token balance for address: {address} and token contract: {contract_address} using endpoint: {endpoint}...")
    
    # Make the API call and return the response
    response = make_api_call(endpoint)

    if response and 'balance' in response:
        print(f"Response from Tatum: {response}")
        return response.get('balance','0')
    else:
        return "0"  # Return 0 if the balance is not found

# Function to fetch the price of a token using Tatum's Market Price API
def fetch_tatum_price(symbol):
    """
    Fetches the price of a given symbol using Tatum's Market Price API.
    """
    endpoint = f"tatum/rate/{symbol}?basePair=USD"
    print(f"Fetching {symbol.upper()} price using Tatum's rate endpoint...")
    response = make_api_call(endpoint)
    return response.get('value') if response else None

# Function to fetch prices for multiple symbols
def fetch_prices(symbols):
    prices = {}
    for symbol in symbols:
        prices[symbol] = fetch_tatum_price(symbol)
    return prices

# Function to fetch balances for multiple ERC-20 tokens
def get_all_token_balances(address):
    """
    Fetch balances for multiple ERC-20 tokens using their contract addresses.
    """
    # Load token contract addresses from a JSON file
    with open('tokens.json', 'r') as file:
        tokens = json.load(file)
    
    balances = {}
    for token, contract_address in tokens.items():
        balance = get_token_balance(address, contract_address)
        balances[token] = balance.get('balance') if balance else "0"
    return balances

# Main function to run the integrations
def main():
    # Specify the contract address for USDT
    usdt_contract_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    
    # Step 1: Generate a new Ethereum wallet and use its xPub
    wallet = generate_wallet("ethereum")

    if wallet and 'xpub' in wallet:
        valid_xpub = wallet['xpub']
        print(f"Generated xPub: {valid_xpub}")

        # Step 2: Derive an Ethereum address from the xPub at index 0
        eth_address = derive_eth_address(valid_xpub, index=0)

        if eth_address:
            print(f"Derived Ethereum Address: {eth_address}")
            
            # Step 3: Fetch the ETH balance of the derived Ethereum addressusing the account endpoint
            print(f"Checking ETH Balance...")
            balance = get_balance("ethereum", eth_address)
            print(f"Ethereum Balance: {balance}")

            # Step 4: Fetch the ERC-20 token balances
            token_balances = get_all_token_balances(eth_address)
            print("ERC-20 Token Balances:", token_balances)

            # Step 5: Fetch prices for multiple symbols
            symbols = ["ETH", "BTC", "SOL", "USDC", "MATIC"]
            prices = fetch_prices(symbols)
            print("Cross-Chain Prices:", prices)

            # Step 6: Fetch the balance of USDT using the contract address
            usdt_balance = get_token_balance(eth_address, usdt_contract_address)    
            print(f"USDT Balance: {usdt_balance}") 

        else: 
            print("Error deriving Ethereum address from xPub.") 
    else:    
        print("Error generating Ethereum wallet.")
     

if __name__ == "__main__":
    main()

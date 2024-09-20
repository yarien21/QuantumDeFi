from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def get_asset_price(asset_id):
    """
    Fetch the current price of a given asset using CoinGecko API.
    
    :param asset_id: The ID of the asset (e.g., 'bitcoin', 'ethereum')
    :return: The current price in USD
    """
    try:
        data = cg.get_price(ids=asset_id, vs_currencies='usd')
        return data[asset_id]['usd']
    except Exception as e:
        print(f"Error fetching price data for {asset_id}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    btc_price = get_asset_price('bitcoin')
    if btc_price:
        print(f"Current Bitcoin price: ${btc_price}")

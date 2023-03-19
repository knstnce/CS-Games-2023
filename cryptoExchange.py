import requests
# https://www.coinapi.io/
API_KEY = 'DAA4E7B5-D800-4CB4-8A7C-9F60AB-42682C'
headers = {'X-CoinAPI-Key': API_KEY, 'Accept': 'application/json'}

# TODO: our header is not being accepted right now!
# Not sure why
# Maybe try getting your own API key...mine doesn't seem to work????

# In the worst case, use ANOTHER API
# GOOD LUCK

def get_all_assets() -> list[dict]:
    url = 'https://rest.coinapi.io/v1/assets'
    return requests.get(url, headers=headers).json()

# Allow any valid asset_id to be passed in (confirm validity based on get_all_assets)
def get_all_current_rates(asset_id: str) -> dict:
    # TODO: check if asset_id in get_all_assets
    url = f'https://rest.coinapi.io/v1/exchangerate/{asset_id}?invert=false'
    # print(requests.get(url, headers=headers))

#1 - Use an API to get the value of various crypto currencies (20 points)
def get_cryptocurrency_values():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    # print(requests.get(url, headers=headers).json())

#2 - Allow users to convert between various crypto currencies (20 points)
def convert_cryptocurrency(*, from_currency: str, from_amount: str, to_currency: str):
    pass
#3 - Allow users to convert between regular and crypto currencies (60 points)
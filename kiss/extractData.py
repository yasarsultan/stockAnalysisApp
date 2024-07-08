import requests 
import os 
# from dotenv import load_dotenv
import pandas as pd 
import yfinance as yf 
from fredapi import Fred 

# load_dotenv() # take environment variable from .env

def load_gold():
    gold_data = yf.download('GOLDBEES.NS', period='10y')
    gold = gold_data[['Close']] # Remove this line if you want to store raw data

    gold.to_csv('kiss/data/gold.csv')

def load_realEstate():
    # fred = Fred()
    Key = os.getenv("FRED_API_KEY") 
    fred = Fred(api_key=Key)

    data = fred.get_series('QINN628BIS', units='pch').fillna(0)
    real_estate = data.to_frame('returns')

    real_estate.to_csv('kiss/data/realEstate.csv')

def load_securities(): 
    # api_key = os.environ.get('EOD_API_KEY')
    api_key = os.getenv("EOD_API_KEY") 

    url = f'https://eodhd.com/api/eod/IN10Y.GBOND?filter=last_close&api_token={api_key}&fmt=json'
    bond_data10y = requests.get(url).json()
    url = f'https://eodhd.com/api/eod/IN5Y.GBOND?filter=last_close&api_token={api_key}&fmt=json'
    bond_data5y = requests.get(url).json()
    url = f'https://eodhd.com/api/eod/IN1Y.GBOND?filter=last_close&api_token={api_key}&fmt=json'
    bond_data1y = requests.get(url).json()
    
    bond_data = pd.DataFrame({'10yBond': [bond_data10y], '5yBond': [bond_data5y], '1yBond': [bond_data1y]})

    bond_data.to_csv('kiss/data/bonds.csv')


def load_equities():
    nifty50 = yf.download('^NSEI', period='10y')
    nifty = nifty50[['Close']] # Remove this line if you want to store raw data

    sensex = yf.download('^BSESN', period='10y')
    sensex = sensex[['Close']] # Remove this line if you want to store raw data

    nifty.to_csv('kiss/data/nifty50.csv')
    sensex.to_csv('kiss/data/sensex.csv')

def load_crypto():
    bitcoin = yf.download('BTC-INR', period='10y')
    bitcoin = bitcoin[['Close']] # Remove this line if you want to store raw data

    bitcoin.to_csv('kiss/data/bitcoin.csv')

load_gold()
load_realEstate()
load_securities()
load_equities()
load_crypto()
print("Script completed successfully")
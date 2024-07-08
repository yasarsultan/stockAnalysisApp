import pandas as pd

def remove_outliers(df):
    Q1 = df.iloc[:, 0].quantile(0.25)
    Q3 = df.iloc[:, 0].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    cleaned_df = df[(df.iloc[:, 0] >= lower_bound) & (df.iloc[:, 0] <= upper_bound)]

    return cleaned_df

def commodities(period):
    gold = pd.read_csv('kiss/data/gold.csv', index_col='Date')

    gold_data = pd.DataFrame()
    gold.index = pd.to_datetime(gold.index)
    last_date = gold.index[-1]
    dates = last_date - pd.DateOffset(years=period)
    actual_date = gold.index.searchsorted(dates)
    gold = gold.iloc[actual_date:]
    gold_data['Close'] = remove_outliers(gold[['Close']]).round(5)
    gold_data.loc[:, 'Cumulative Returns'] = gold_data['Close'].pct_change().fillna(0).cumsum() * 100
    
    return gold_data


def real_estate(period):
    publicProperty = pd.read_csv('kiss/data/realEstate.csv', names=['Date', 'returns'], skiprows=1, index_col='Date')
    
    publicProperty.index = pd.to_datetime(publicProperty.index)
    last_date = publicProperty.index[-1]
    dates = last_date - pd.DateOffset(years=period)
    actual_date = publicProperty.index.searchsorted(dates)
    publicProperty = publicProperty.iloc[actual_date:]
    propertydata = pd.DataFrame()
    propertydata['Cumulative Returns'] = publicProperty['returns'].cumsum()

    return propertydata


def securities(period):
    bonds = pd.read_csv('kiss/data/bonds.csv', index_col=0)
    record = [0]

    if period == 1:
        bond = bonds.loc[0, '1yBond']
    elif period == 5:
        bond = bonds.loc[0, '5yBond']
    else:
        bond = bonds.loc[0, '10yBond']
    for _ in range(period):
        record.append(bond + record[-1])
    
    bondData = pd.DataFrame({'Returns': record})

    return bondData


def equities(period, index='nifty50'):
    data = pd.DataFrame()

    if index == 'nifty50':
        nifty50 = pd.read_csv('kiss/data/nifty50.csv', index_col='Date')

        nifty50.index = pd.to_datetime(nifty50.index)
        last_date = nifty50.index[-1]
        date = last_date - pd.DateOffset(years=period)
        actual_date = nifty50.index.searchsorted(date)
        data = nifty50.iloc[actual_date:]
        data['Close'] = remove_outliers(nifty50[['Close']]).round(5)
        data.loc[:, 'Cumulative Returns'] = data['Close'].pct_change().fillna(0).cumsum() * 100

    elif index == 'sensex':
        sensex = pd.read_csv('kiss/data/sensex.csv', index_col='Date')

        sensex.index = pd.to_datetime(sensex.index)
        last_date = data.index[-1]
        date = last_date - pd.DateOffset(years=period)
        actual_date = sensex.index.searchsorted(date)
        data = sensex.iloc[actual_date:]
        data['Close'] = remove_outliers(sensex[['Close']]).round(5)
        data.loc[:, 'Cumulative Returns'] = data['Close'].pct_change().fillna(0).cumsum() * 100
        
    return data



def crypto(period):
    bitcoin = pd.read_csv('kiss/data/bitcoin.csv', index_col='Date')

    bitcoin.index = pd.to_datetime(bitcoin.index)
    last_date = bitcoin.index[-1]
    date = last_date - pd.DateOffset(years=period)
    actual_date = bitcoin.index.searchsorted(date)
    data = bitcoin.iloc[actual_date:]
    data['Close'] = remove_outliers(bitcoin[['Close']]).round(5)
    data.loc[:, 'Cumulative Returns'] = data['Close'].pct_change().fillna(0).cumsum() * 100
    
    return data
import tdameritrade as td
from keys import PyScanner
import requests
import pandas as pd
url = "https://api.tdameritrade.com/v1/instruments"

df  = pd.read_excel('csvSymbol.csv')
symbol  = df['symbole'].values.tolist()

start = 0 
end   = 0

while start < len(symbol):
    tickers = symbol[start:end]
    payload  = {
        'apikey' : PyScanner.key,
        'symbol' : 'GOOG',
        'projection' : 'fundamental'
    }


    result  = requests.get(url,params=payload)
    unpackJSON = result.json()
    start = end 
    end  += 500

print(unpackJSON['GOOG']['fundamental'])
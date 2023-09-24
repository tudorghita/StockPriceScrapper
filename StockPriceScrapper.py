
import pip._vendor.requests
from bs4 import BeautifulSoup
import json

mystocks = ['VAST.L', 'ICON.L', 'PREM.L', 'BZT.L', 'ASPL.L']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
    url = f'https://uk.finance.yahoo.com/quote/{symbol}'

    r = pip._vendor.requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'price' :  soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('span')[0].text,
    'change' : soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('span')[1].text,
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)

print('Finalized')
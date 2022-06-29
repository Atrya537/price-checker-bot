from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/huanuo-hnssk4-black/p/15Z-01XB-00049?Item=9SIAJDS9C72608&cm_sp=Homepage_dailydeals-_-P1_9SIAJDS9C72608-_-06292022&quicklink=true'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

def get_current_price():
    prices = doc.find(text='$').parent
    itemPrice = prices.find('strong').text
    return itemPrice

def current_price_to_int():
    intCurrentPrice = []

    currentPriceAsArray = get_current_price().split(',')
    for i in currentPriceAsArray:
        if (',' not in i):
            intCurrentPrice.append(i)

    return (int(''.join(intCurrentPrice)))

def get_original_price():
    priceWas = doc.find_all('span', {'class': 'price-was-data'})[0]
    return(priceWas.text)

def original_price_to_int():
    intOriginalPrice = []
    
    originalPriceAsArray = list(get_original_price())
    for i in originalPriceAsArray:
        if (i.isdigit()):
            intOriginalPrice.append(i)

    del intOriginalPrice[-2:]
    return int(''.join(intOriginalPrice))

priceDifference = original_price_to_int() - current_price_to_int()

if (original_price_to_int() > current_price_to_int()):
    print(f'Your item is ${priceDifference} off!')
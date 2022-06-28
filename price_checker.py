from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3987-kr/p/N82E16814487526?Item=N82E16814487526&Description=rtx%203090&cm_re=rtx_3090-_-14-487-526-_-Product&quicklink=true'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

def get_current_price():
    prices = doc.find(text='$').parent
    gpuPrice = prices.find('strong').text
    return gpuPrice

def convert_current_price_to_int():
    currentPriceToInt = []

    currentPriceAsArray = get_current_price().split(',')
    for i in currentPriceAsArray:
        if (',' not in i):
            currentPriceToInt.append(i)

    return (int(''.join(currentPriceToInt)))

#TODO: FIX THIS (filter out dollar sign and comma to convert price to int)
def get_original_price():
    priceWas = doc.find_all('span', class_='price-was-data')
    parent = priceWas[0].parent
    originalPrice = parent.find('span').text

def convert_original_price_to_int():
    originalPriceToInt = []
    
    originalPriceAsArray = get_original_price().split(',')
    for i in originalPriceAsArray:
        if (',' not in i or '$' not in i):
            originalPriceToInt.append(i)

    print(originalPriceToInt)


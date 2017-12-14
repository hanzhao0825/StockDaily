import numpy as np
import urllib2
import re

def fetchPriceDataFromYahoo(symbol, d):
    try:
        url = 'https://finance.yahoo.com/quote/' + symbol + '/history?p=' + symbol
        response = urllib2.urlopen(url)
        html = response.read()
    except Exception as e:
        html = ''
    pattern = re.compile(r'"adjclose":(\d*\.\d*)}')
    string_data = pattern.findall(html)
    data = [float(price) for price in string_data]

    result = np.array(data[:d])
    return result

def readSymbolListFromTXT(fn):
    lines = []
    with open(fn, 'r') as f:
        lines = f.read().splitlines()
    return lines

def MA(price_data, d):
    return np.average(price_data[:d])

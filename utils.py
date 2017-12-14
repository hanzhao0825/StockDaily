import numpy as np
import urllib2
import re

def fetchPriceDataFromYahoo(symbol, d):
    try:
        url = 'https://finance.yahoo.com/quote/' + symbol + '/history?p=' + symbol
        response = urllib2.urlopen(url, timeout = 10)
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

def readFilterFromTXT(fn):
    fi = ''
    with open(fn, 'r') as f:
        fi = f.read()
    return fi

def compare_MA5_MA20(symbol):
    print symbol + '\t',
    price_data = fetchPriceDataFromYahoo(symbol, 20)
    MA_5 = MA(price_data, 5)
    MA_20 = MA(price_data, 20)
    print '%.3f\t%.3f\t' % (MA_5, MA_20),
    if MA_5 > MA_20:
        print 'BUY'
    else:
        print 'SELL'

def MA(price_data, d):
    return np.average(price_data[:d])

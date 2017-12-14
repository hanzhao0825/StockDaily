from screener import screen
from utils import *

'''
Check current stocks
'''
print 'Checking current stocks'
current_symbol_list = readSymbolListFromTXT('current.txt')
print current_symbol_list
for symbol in current_symbol_list:
    print symbol
    price_data = fetchPriceDataFromYahoo(symbol, 30)
    MA_5 = MA(price_data, 5)
    MA_20 = MA(price_data, 20)
    print MA_5, MA_20

print ''
print 'Checking new stocks'
f = 'f=exch_nasd,fa_debteq_u0.9,fa_epsyoy_high,fa_pe_u25,fa_peg_low,sh_price_o5&ft=4'
new_symbol_list = screen(f)

print new_symbol_list

for symbol in new_symbol_list:
    print symbol
    price_data = fetchPriceDataFromYahoo(symbol, 30)
    MA_5 = MA(price_data, 5)
    MA_20 = MA(price_data, 20)
    print MA_5, MA_20

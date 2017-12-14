from screener import screen
from utils import *

'''
Check current stocks
'''
print 'Checking current stocks'
current_symbol_list = readSymbolListFromTXT('current.txt')
print current_symbol_list
for symbol in current_symbol_list:
    compare_MA5_MA20(symbol)
print ''


'''
Check new stocks
'''
print 'Checking new stocks'
f = readFilterFromTXT('filter.txt')
new_symbol_list = screen(f)
print new_symbol_list
for symbol in new_symbol_list:
    compare_MA5_MA20(symbol)

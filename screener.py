import urllib2
import re

def screen(f):
    f = 'f=exch_nasd,fa_debteq_u0.9,fa_epsyoy_high,fa_pe_u25,fa_peg_low,sh_price_o5&ft=4'
    result = []
    url = 'https://finviz.com/screener.ashx?v=111&' + f
    response = urllib2.urlopen(url)
    html = response.read()
    pattern = re.compile(r'Total: </b>(\d*) #1')

    total = int(pattern.search(html).group(1))

    for start in range(1, total, 20):
        url = 'https://finviz.com/screener.ashx?v=111&' + f + '&r=' + str(start)
        response = urllib2.urlopen(url)
        html = response.read()
        pattern = re.compile(r'screener-link-primary">(\w*)</a>')
        symbol_list = pattern.findall(html)
        result.extend(symbol_list)

    return result

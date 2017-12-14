import urllib2
import re

def screen(f):
    result = []
    url = 'https://finviz.com/screener.ashx?' + f
    print url
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

import urllib
import re

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    # print content
    m = re.search(r'id="ref_(\d*)_l">(.*?)<', content)
    # m = re.search(r',rows:[{id:"(\d*)",values:["(.*)","(.*?)","(.*)","(.*)","(.*)","(.*)","","(.*)","(.*)","(\d*)","(.*)"]}', content)

    if m:
    	quote = m.group(2)
    else:
        quote = 'no quote available for: ' + symbol
    return quote

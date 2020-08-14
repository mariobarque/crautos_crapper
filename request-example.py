import requests

cookies = {
    '_ga': 'GA1.2.1086318761.1590757962',
    '_fbp': 'fb.1.1590757962289.248230899',
    '__gads': 'ID=fe8060fa0c0f6082:T=1590757975:S=ALNI_MZC_qkGTHGHfSVyeLa-J_sVz3G9SQ',
    '__auc': 'feaaa7fe1726090fe89574321ea',
    '_fbc': 'fb.1.1597238745016.IwAR1oKmwcuzq4lIGQpq60OVOUFb1wxlmXMFEEW6xtX__ka8nc_5lB5y7p-F0',
    '_gid': 'GA1.2.2010079522.1597367155',
    '_gat': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://crautos.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://crautos.com/autosusados/',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'brand': '00',
  'modelstr': '',
  'style': '00',
  'fuel': '0',
  'trans': '0',
  'financed': '00',
  'recibe': '0',
  'province': '0',
  'doors': '0',
  'yearfrom': '1960',
  'yearto': '2020',
  'pricefrom': '100000',
  'priceto': '200000000',
  'orderby': '0',
  'lformat': '0'
}

response = requests.post('https://crautos.com/autosusados/searchresults.cfm', headers=headers, cookies=cookies, data=data)

print(response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://crautos.com/autosusados/searchresults.cfm?p=1', headers=headers, cookies=cookies, data=data)

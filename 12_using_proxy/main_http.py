import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    html =requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('tbody').find_all('tr')
    #trs = soup.find('table', id = 'proxylisttable').find_all('tr')[1:11]
    proxies = []
    for tr in trs:
        tds = tr.find_all('td')
        if tds[6].text.strip() == 'no':
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            schema = 'http'
            proxy = {'schema':schema,'address':ip + ':' + port}
            proxies.append(proxy)
        else:
            continue
    return choice(proxies)

def get_html(url):
    #proxies = {'http/https':'ipaddress:port'}
    p = get_proxy()#returns {'schema':'','address':''}
    proxy = {p['schema']:p['address']}
    r =requests.get(url,proxies=proxy,timeout=5)
    #return r.json()['origin']
    return r.json()['ip']


def main():
   #url = 'http://httpbin.org/ip'
    url ='https://ip4.seeip.org/json'
    print(get_html(url))


if __name__=='__main__':
    main()

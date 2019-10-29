import requests
from bs4 import BeautifulSoup
import csv,re

def get_html(url):
    r=requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)

def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],data['url'],data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', id='currencies').find('tbody').find_all('tr')#getting all rows in table
    for tr in tds:
        #for each row we get all td's in this row
        tds = tr.find_all('td')
        try:
            name = tds[1].find('a', class_='currency-name-container').text
        except:
            name = ''
        try:
            #url to the currency page
            url = 'https://coinmarketcap.com' + tds[1].find('a', class_='currency-name-container').get('href')
        except:
            url = ''
        try:
            price = tds[3].find('a').get('data-usd').strip()
        except:
            price = ''
        data = {'name':name,'url':url,'price':price}
        write_csv(data)

#in/out
def main():
    url = 'https://coinmarketcap.com/'

    #method ll: dealong with pagination
    ##scenario 2: unkown amunt of pages
    while True:
        get_page_data(get_html(url))
        soup = BeautifulSoup(get_html(url),'lxml')

        try: #we'll use RE to beat this thing.
            pattern = 'Next'
            url = 'https://coinmarketcap.com' + soup.find('ul', class_='pagination').find('a', text=re.compile(pattern)).get('href')#using RE if 'a' doesn't contain text 'Next' then we don't get 'href'
        except:
            #in case we diodn't find 'Next' we break from the cycle
            break


if __name__=='__main__':
    main()

import requests
from bs4 import BeautifulSoup
import csv

#
def get_html(url):
    r= requests.get(url)
    if r.ok: #200 #403 #404
        return r.text
    print(r.status_code)#print if url code(!200) is bad.

def get_page_data(html):
    soup= BeautifulSoup(html, 'lxml')

    lis = soup.find_all('li', class_='col-6')
    #print(len(lis)) # 9 on 1 page
    for li in lis:
        try:
            name = li.find('div',class_='theme-card__footer').find('a', class_='theme-card__title').text
        except:
            name = ''
        try:
            url = li.find('div', class_='theme-card__footer').find('a').get('href')
        except:
            url = ''
        try:
            category = li.find('div', class_='theme-card__footer').find('ul').find('a').text
        except:
            category = ''
        try:
            price = li.find('p', class_='theme-card__price').find('span', class_='woocommerce-Price-amount').text.strip('$')
        except:
            price = ''

        data = {'name':name,'url':url,'category':category,'price':price}
        write_csv(data)

#export to csv
def write_csv(data):
    with open('bootstrap_price.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],data['url'],data['category'],data['price']))


def main():
    pattern = 'https://themes.getbootstrap.com/shop/page/{}' #/{}.php
    #adding pagination (method 1)
    for i in range(0,7):
        url = pattern.format(str(i))
        #print(url)


        get_page_data(get_html(url))


if __name__=='__main__':
    main()

import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    r = requests.get(url, headers=user_agent)
    return r.text

def write_csv(data):
    with open ('testimonials.csv','a') as f:
        order = ['author','since']
        writer = csv.DictWriter(f,fieldnames=order)
        writer.writerow(data)

def get_articles(html):
    soup = BeautifulSoup(html,'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')

    return ts #[] or [a,b,c]

def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since=''
        try:
            author= t.find('p', class_='testimonial-author').text.strip()
        except:
            author=''
        data = {'author':author,'since':since}
        write_csv(data)


def  main():

#    1.get container with testimonials and getting list of testimonials
#    2.if list exist we keep parsing
#    3.if list is empty we break to end cycle
    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/?themify_builder_infinite_scroll=yes'.format(str(page))
        articles = get_articles(get_html(url))# [] or [1,2,3 ..]
        if articles:
            get_page_data(articles)
            pages = page + 1
        else:
            break


if __name__== '__main__':
    main()



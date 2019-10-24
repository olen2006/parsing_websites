import requests
from bs4 import BeautifulSoup
import csv

#input url | output r.text (html)
def get_html(url):
    r = requests.get(url)
    return r.text

#normalizing data for export in csv later on
def refind(s):
    #1,666 total ratings
    r = s.split()[0]
    #get rid of comma
    #result=r.replace(',','')
    return r.replace(',','')

def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews'],
                         data['description']
                         ))

#input html | output dictionary
def get_data(html):
    #passing in class of bs4
    soup = BeautifulSoup(html,'lxml')
    #!<class 'bs4.BeautifulSoup'>
   #featured = soup.find('div', id='page').find('header').find('section').text
    #let's find all popular
    popular = soup.find_all('section')[3]#find_all cratesa list of sections
    plugins = popular.find_all('article')#4
    for plugin in plugins:
       #[plugin1, plugin2, plugin3, plugin4]
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        body = plugin.find('p').text

        r = plugin.find('span',class_='rating-count').find('a').text  #need separate function
        rating = refind(r)

       #to geather all the data we need to use dictionary
        data = {'name': name,
                'url': url,
                'reviews': rating,
                'description': body
                }
        #print (data)
        write_csv(data)


#Main Hub of all functions In/Out
def main():
    url='https://wordpress.org/plugins/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()

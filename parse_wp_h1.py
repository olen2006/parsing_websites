import requests
from bs4 import BeautifulSoup

#input url | output r.text (html)
def get_html(url):
    r = requests.get(url)
    return r.text

#input html | output h1
def get_data(html):
    #passing in class of bs4
    soup = BeautifulSoup(html,'lxml')
    #!<class 'bs4.BeautifulSoup'>
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text

    return h1 #!<class 'bs4.element.Tag'>


#Main Hub of all functions In/Out
def main():
    url='https://wordpress.org'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()

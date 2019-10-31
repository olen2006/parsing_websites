import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    #return r.text# r.header
    return r



def write_csv(data):
    with open('youtube_list.csv', 'a') as f:
        order = []
        writer = csv.DictWrite(f,fieldnames=order)
        writer.writerow(data)


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        #if we deal with json object
        html = response.json()['content_html']
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('h3',class_='yt-lockup-title')

    for item in items:
        name = item.text.strip()
        url = item.find('a').get('href')
        print(name)
def get_next(response):
    if 'html' in response.header['Content-Type']:
        html = reponse.text
    else:
        html = response.json()['load_more_widjet_html']
    soup = BeautifulSoup(html,'lxml')
    try:
        url = soup.find('button')



def main():
    url = 'https://www.youtube.com/channel/UCrp_UI8XtuYfpiqluWLD7Lw/videos' #'https://www.youtube.com/user/zaemiel/videos'#Molchanov channel
    #get_page_data(get_html(url))
    while True:
        response = get_html(url)
        get_response_data(response)
        url = get_next(response)


if __name__ =='__main__':
    main()

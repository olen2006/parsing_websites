import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    #return r.text# r.header
    return r



def write_csv(data):
    with open('youtube_list.csv', 'a') as f:
        order = ['name','url']
        writer = csv.DictWriter(f,fieldnames=order)
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

        data = {'name':name, 'url':url}
        write_csv(data)

def get_next(response):
    #check type of response html or json
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        #button that loads more pages
        html = response.json()['load_more_widget_html']
    soup = BeautifulSoup(html,'lxml')
    try:
        url ='https://youtube.com' + soup.find('button', class_='load-more-button').get('data-uix-load-more-href')#we received browse_ajax link
    except:
        url = ''
    return url

def main():
    #rl = 'https://youtube.com/browse_ajax?action_continuation=1&continuation=4qmFsgI0EhhVQ09tNF9BbkxQTEVCVnJiby0tTjdrUEEaGEVnWjJhV1JsYjNNZ0FEZ0JlZ0V5dUFFQQ%253D%253D&direct_render=1'
    url = 'https://www.youtube.com/user/coolpropaganda/videos'
    #get_page_data(get_html(url))
    while True:
        #get data from one page
        response = get_html(url)
        #parse data from this page
        get_page_data(response)
        #call function to load second page(url will be changed)
        url = get_next(response)
        if url:
            continue
        else:
            break


if __name__ == '__main__':
    main()


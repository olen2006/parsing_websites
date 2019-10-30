import requests
import csv
from multiprocessing import Pool

def get_html(url):
    r=requests.get(url)
    return r.text

def write_csv(data):
    with open('websites.csv', 'a')as file:
        order = ['name','url','description','traffic','percent']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)

def get_page_data(text):
    data = text.strip().split('\n')[1:]#split removes \n\n in the beginning and end
    for row in data:
        columns = row.strip().split('\t')
        #print(columns)
        name = columns[0]
        url = columns[1]
        description = columns[2]
        traffic = columns[3]
        percent = columns[4]

        data = {'name':name,
                'url':url,
                'description':description,
                'traffic':traffic,
                'percent':percent
                }

        write_csv(data)

def make_all(url):
    text = get_html(url)
    get_page_data(text)

def main():
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    # make sure page 0 and 1 are not the same one!
    urls=[url.format(str(i)) for i in range(1,4772)]#last page 4771
    #print(urls)

    #50 workers
    with Pool(50) as p:
        p.map(make_all,urls)

if __name__=='__main__':
    main()

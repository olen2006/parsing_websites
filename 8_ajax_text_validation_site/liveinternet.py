import requests
import csv

def get_html(url):
    r = requests.get(url)
    return r.text
def write_csv(data):
    with open('websites.csv','a') as f:
        order =['name','url','description','traffic','percent']
        writer = csv.DictWriter(f,fieldnames=order)
        writer.writerow(data) # {'name':'Oleg','last_name':'Fortochnik'}

def main():

    #total pages 4426
    for i in range(0,4427):

        ########That was for  one page###############
        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
        response = get_html(url)
        data = response.strip().split('\n')[1:]#split removes \n\n in the beginning and end
        #print(data)
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


if __name__ =='__main__':
    main()



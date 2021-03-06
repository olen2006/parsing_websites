import csv

def write_csv(data):
    with open('names.csv','a') as file:
        #https://docs.python.org/3/library/csv.html#csv.writer
        writer = csv.writer(file)
        #Method 1
        writer.writerow((data['name'], data['surname'], data ['age']))



def write_csv2(data):
    with open('names.csv', 'a') as file:
        order = ['name','surname','age']
        #Method 2
        #DickWriter is not in order, so we use parameter
        writer.csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)
def main():
    #dictionaries
    d = {'name':'Oleg', 'surname':'Fortochnik', 'age':30}
    d1 = {'name':'James', 'surname':'Cole', 'age':24}
    d2 = {'name':'Olaf', 'surname':'Zimmerman', 'age':18}

    l = [d, d1, d2]

    for i in l:
        write_csv(i)
    #Reading from file
    with open('datasheet.csv') as file:
        fieldnames = ['name','url','price']
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            print(row)

if __name__=='__main__':
    main()

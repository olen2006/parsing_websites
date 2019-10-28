import csv
from peewee import *

#PostgresqlDatabase and Model imported from peewee
try:
    print('Connecting...')
    db = PostgresqlDatabase(database='test', user='postgres', password='password', host='127.0.0.1')
except:
    print('Error: Connection Failed to DB')
#creating class that will represent our table in DB
class Coin(Model):
    #http://docs.peewee-orm.com/en/latest/peewee/query_examples.html#model-definitions
    name = CharField()#max_lenght=255 or 10 etc
    url = TextField()
    price = CharField()
    #connecting class with db
    class Meta:
        database=db



def main():
    db.connect()
    db.create_tables([Coin])#creating tables in DB
    with open ('cmc.csv') as f:
        order = ('name','url','price')
        reader = csv.DictReader(f, fieldnames=order)
        coins = list(reader)
#        for row in coins:      #Method #1
#            #print(row)
#            coin = Coin(name=row['name'],url=row['url'],price=row['price'])
#            coin.save()

#        Method #2 using peewee transactions, gor for live parsing
        with db.atomic():
            #for row in coins:
            #    Coin.create(**row)
            ############################################
            #Method 3 fastest. but may not work during live parsing
            for index in range(0,len(coins),100):
                Coin.insert_many(coins[index:index+100]).execute()

if __name__ == '__main__':
    main()

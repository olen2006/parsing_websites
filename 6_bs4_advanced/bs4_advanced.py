from bs4 import BeautifulSoup
import re

# .find()
# .find_all()

# .parent
# .find_parent()

# .parents
# .find_parents()

# .find_next_sibling()
# .find_previous_sibling()

def get_copywriter(tag):
    whois =tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None

def get_salary(s):
    #salary: 2700 usd per month
    # r - row data
    pattern = r'\d{1,9}'
    #salary = re.findall(pattern, s)[0]
    salary = re.search(pattern, s).group()
    print(salary)

#    ^ - beginning of the row
#    & - end of the row
#    . - any symbol
#    + - any amount of symbols
#    '\d' - number
#    '\w' - letters,numbers

#main hub in/out
def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')
    #Method 1
#    copywriters = []
#    persons = soup.find_all('div', class_='row')
#
#    for person in persons:
#        cw = get_copywriter(person)
#        if cw:
#            copywriters.append(cw)
#    print(copywriters)

    #salary = soup.find_all('div', {'data-set':'salary'})
    salary = soup.find_all('div', text=re.compile('\d{1,9}'))
    print(salary)
    for i in salary:
        get_salary(i.text)


if  __name__ == '__main__':
    main()


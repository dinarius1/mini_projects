#Task 1

#неправильный вариант
# import requests
# source = requests.get('https://stackoverflow.com/questions')
# print(source.status_code)

# правильный вариант:
# import requests 
# source = requests.get('https://stackoverflow.com/questions').status_code 
# print(source)

#Task 2
# import requests
# from bs4 import BeautifulSoup
# sourse = requests.get('http://www.example.com/').text
# soup = BeautifulSoup(sourse, 'lxml')
# print(f"h1: {soup.h1.text}")
# print(f"p: {soup.p.text}")
# print(f"a: {soup.a.get('href')}")

#Task 3

# import requests
# from bs4 import BeautifulSoup
# source = requests.get('https://www.wikipedia.org/').text
# soup = BeautifulSoup(source, 'lxml')
# language = soup.find('div', class_ = 'central-featured-lang lang4').find('a').find('strong').text
# number = soup.find('div', class_ = 'central-featured-lang lang4').find('a').find('small').find('bdi').text
# artical = soup.find('div', class_ = 'central-featured-lang lang4').find('a').find('small').find('span').text
# # soup.find('div',{'class_' : 'central-featured-lang lang4'}.find('lang4') - почему, когда так пишешь выходит ошибка,

# print(f'{language} \n{number} {artical}')

#Task 4
# import requests
# from bs4 import BeautifulSoup
# def getTitle(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, 'lxml').find('h1')
#     if soup == None:
#         return 'Title could not be found'
#     return soup

# # print(getTitle('https://www.w3resource.com/'))
# print(getTitle('http://www.example.com/'))


# Задание 5

# import requests
# from bs4 import BeautifulSoup

# source = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(source, 'lxml')


# category_list = soup.find('div', class_="moduletable").find('ul').find('li').text
# print(category_list)

# Задание 6
    
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.imdb.com/chart/top').text
soup = BeautifulSoup(source, 'lxml')

title_list = soup.find('div', class_="lister").find('table').find_all('td', class_="titleColumn")

def get_link(title_list, name : str):
    titles = []
    # film_links = []
    for el in title_list:
        # titles.append(el.find('a').text)
        title = el.find('a').text 
        if title.startswith(name):
            link = el.find('a').get('href')
    return link



    # for i in titles:
    #     if name.startswith(i):
    #         link = el.find('a').get('href')
        
    #     if name in el.find('a').text:
    #         link = el.find('a').get('href')
    # return link

        # title_list.append(el.find('a').text)
        # film_links.append(el.find('a').get('href'))
    # if name in title_list:

print(get_link(title_list, 'shawshank'))
    # if name in title_list:
        
    #     return 




s1 = ['Kristina Fedorova']
s = 'Kristina'
for i in s1:
    if i.startswith(s):
        print('True')
    else:
        print('F')


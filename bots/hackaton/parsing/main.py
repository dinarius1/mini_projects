import requests
from bs4 import BeautifulSoup

# source = requests.get('https://kaktus.media/?lable=8&date=2023-03-08&order=time').text
# soup = BeautifulSoup(source, 'lxml')

BASE_URL = 'https://kaktus.media'

def get_soup(url:str) -> BS:
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    return soup

def get_previous_page(url : str) -> int:
    soup = get_soup(url)
    last = soup.find('li', {'class' : 'last'})
    return int(last.text)


def main():
    category = '/noutbuki'
    data = {}
    last_page = get_previous_page(BASE_URL + category)
    for page in range(1,last_page + 1):
        url = BASE_URL + category + '?page=' + str(page)
        print(url)
        one_page_data = get_all_products_from_page(url)
        data[page] = one_page_data
    write_to_json(data)
main()

#функция которая показывает
# 1.нумерацию новости
# 2.заголовок новости

def get_titles_news(url) -> dict:
    url = 
    title = soup.find('div', class_="Tag--articles").find_all('a',class_="ArticleItem--name")

    all_titles = [el.text.strip('\n') for el in title]

    numbers = 1

    return all_titles
print(get_titles_news(soup))


#функция которая показывает
# 1. описание новости
# 2. фотографии новости

# def get_all_news_from_page(soup:BS) -> list:
#     res = []
#     box = soup.find('div', {'class':'list-view'})
#     products = box.find_all('div', {'class':'product_listbox'})
#     for product in products:
#         product_info = get_product_info(product)
#         res.append(product_info)
#     return res
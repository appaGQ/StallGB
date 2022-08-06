from requests import Session
from bs4 import BeautifulSoup
from db import list_of_iphone_12_wt_colour, list_of_iphone_13_wt_colour

url_BG_airpods = "https://biggeek.ru/catalog/apple-airpods"
url_BG_iphone_12 = 'https://biggeek.ru/catalog/apple-iphone-12'
url_BG_iphone_13 = 'https://biggeek.ru/catalog/apple-iphone-13'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2520 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}
session = Session()


# Парсинг страницы с наушнками
def get_data_airpods():
    # Отправление запроса и получение списка цен
    response_headphones = session.get(url=url_BG_airpods, headers=headers)
    soup = BeautifulSoup(response_headphones.content, 'html.parser')
    info_card = soup.find_all('div', class_='catalog-card')
    flag = 1
    # Извлечение первых 4 наименований и цен карточек товара
    ls_of_price = ''
    for items in info_card:
        title_card = items.find('a', class_='catalog-card__title cart-modal-title').text
        cost_card = items.find('b', class_='cart-modal-count').text
        # print(title_card ,":" , cost_card)
        ls_of_price += str(flag) + '. ' + title_card[9:] + ': ' + cost_card + '\n'
        flag += 1
        if flag == 5:
            flag = 1
            break
    return ls_of_price


# Парсинг страницы айфонов 12
def get_data_iphone_12(colour):
    # Отправление запроса и получение списка цен
    response_12 = session.get(url=url_BG_iphone_12, headers=headers)
    soup = BeautifulSoup(response_12.content, 'html.parser')
    info_card = soup.find_all('div', class_='catalog-card')
    flag = 1
    ls_of_price_iphone_12 = ''
    list_colors = [item.format(colour) for item in list_of_iphone_12_wt_colour]
    for items in info_card:
        title_card = items.find('a', class_='catalog-card__title cart-modal-title').text
        cost_card = items.find('b', class_='cart-modal-count').text
        if title_card in list_colors:
            ls_of_price_iphone_12 += str(flag) + '. ' + title_card[6:] + ': ' + cost_card + '\n'
            flag += 1
            if flag == 4:
                flag = 1
                break
    return ls_of_price_iphone_12


# Парсинг страницы айфонов 13
def get_data_iphone_13(colour):
    # Отправление запроса и получение списка цен
    response_13 = session.get(url=url_BG_iphone_13, headers=headers)
    soup = BeautifulSoup(response_13.content, 'html.parser')
    info_card = soup.find_all('div', class_='catalog-card')
    flag = 1
    ls_of_price_iphone_13 = ''
    list_colors = [item.format(colour) for item in list_of_iphone_13_wt_colour]
    for items in info_card:
        title_card = items.find('a', class_='catalog-card__title cart-modal-title').text
        cost_card = items.find('b', class_='cart-modal-count').text
        if title_card in list_colors:
            ls_of_price_iphone_13 += str(flag) + '. ' + title_card[6:] + ': ' + cost_card + '\n'
            flag += 1
            if flag == 4:
                flag = 1
                break
    return ls_of_price_iphone_13
print(get_data_iphone_13('Midnight'))


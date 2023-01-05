# import libraries
from bs4 import BeautifulSoup
import requests

html_text = requests.get('http://ida4ay.com/ru').text  # query variable
soup = BeautifulSoup(html_text, 'lxml')  # make a request and get html
# find one item
tea = soup.find('div', class_ = 'js-product t-store__card t-store__stretch-col t-store__stretch-col_25 t-align_left t-item t-animate t-animate_started')
tea_name = tea.find('a', class_ = 'js-store-prod-name js-product-name t-store__card__title t-name t-name_xs')
print(tea_name)
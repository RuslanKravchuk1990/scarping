# import libraries
from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/detail_basic/' #website address variable

response = requests.get(url)  # query variable

soup = BeautifulSoup(response.text, 'lxml')  # make a request and get html

data = soup.find('div', class_ = 'card mt-4 my-4') # find one item

name = data.find('h3', class_ = 'card-title').text #find the name of the selected product

price = data.find('h4').text #find the price of the selected product

url_img = 'https://scrapingclub.com' + data.find('img', class_ = 'card-img-top img-fluid').get('src') #find the link of the selected product
print(name + '\n' + price + '\n' + url_img + '\n\n')
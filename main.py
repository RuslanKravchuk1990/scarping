# import libraries
from bs4 import BeautifulSoup
import requests
from time import sleep

list_course_url = []

 #to search for each item on multiple pages, you can use a for loop
for count in range(0,3):
    sleep(1)
    url = f'https://scrapingclub.com/blog/?page={count}' #website address variable #url = 'https://scrapingclub.com/exercise/detail_basic/'

    response = requests.get(url)  # query variable
    soup = BeautifulSoup(response.text, 'lxml')  # make a request and get html
    data = soup.find_all('div', class_ = 'col-lg-8')

#to search for each product on the page, you can use the for cycle
    for i in data:

          course_url = 'https://scrapingclub.com' + i.find('a').get('href')
          list_course_url.append(course_url)

for course_url in list_course_url:

    response = requests.get(url)  # query variable
    soup = BeautifulSoup(response.text, 'lxml')  # make a request and get html
    data = soup.find('div', class_ = 'container mt-4')
    name = data.find('div', class_ = 'card my-4').text.replace('\n', '') #find the name of the selected product
    course_name = data.find('h2').text #find the price of the selected product
    url_img = 'https://scrapingclub.com' + data.find('img', class_ = 'card-img-top img-fluid').get('src') #find the link of the selected product
    print(name + '\n' + course_name + '\n' + url_img + '\n\n')

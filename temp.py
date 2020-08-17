import requests
from bs4 import BeautifulSoup
from carparser import CarParser

#car = CarParser.parse_car()

url = 'https://crautos.com/autosusados/cardetail.cfm?c=3167619'

response = requests.request("GET", url)
soup = BeautifulSoup(response.text, 'html.parser')
images_table = soup.find_all('table', attrs={'class':'table-responsive table-striped table-bordered'})
no_image = '/rimages/nopiclg.jpg'
first_image = images_table[0].contents[3].contents[1].contents[1].attrs['src']
if no_image == first_image:
    print('No Image')
else:
    print('Image')
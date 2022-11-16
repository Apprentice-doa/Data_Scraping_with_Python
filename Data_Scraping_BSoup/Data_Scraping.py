#Importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests



def scrape(url): # creates a function for url
    require = requests.get(url) # gets the required url 
    soup = BeautifulSoup(require.text, "html.parser") # modifies the url for scraping and parses it

    for index, product in enumerate(soup.findAll('a', href=True, attrs={'class': 'core'})):
        name = product.find("h3", attrs={'class': 'name'})
        print('No.', index, 'Name:', name.text.upper())

        price = product.find('div', attrs={'class': 'prc'})
        print('      Price:', price.text)
        print(
        "---------------------------------------------------------------------------------------------------------------------------")
scrape("https://jiji.ng/tv-dvd-equipment?query=electronics&filter_attr_272_type=TVs")



#Importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

item = []
def scrape(url): # creates a function for url
    require = requests.get(url) # gets the required url 
    soup = BeautifulSoup(require.text, "html.parser") # modifies the url for scraping and parses it

    for index, product in enumerate(soup.findAll('a', href=True, attrs={'class': 'core'})):
        name = product.find("div", attrs={'class': 'name'})
        price = product.find('div', attrs={'class': 'prc'})
        price = price.text
        price = price[1:]
        price = float(price.replace(",", ""))

        if name is not None:
          name = name.text.upper()
          print('No.', index, 'Name:', name, '      Price:', price) 
          item.append([name, price])
          df = pd.DataFrame(item, columns = ['Names', 'Price'])
          df.to_csv('items.csv')

scrape("https://www.jumia.com.ng/computing/")


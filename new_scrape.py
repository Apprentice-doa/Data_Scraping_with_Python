#Importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

require = requests.get("https://www.jumia.com.ng/electronics/") # gets the required url 
print(require)
soup = BeautifulSoup(require.text, "html.parser") # modifies the url for scraping and parses it
print(soup)
for index, product in enumerate(soup.findAll('a', href=True, attrs={'class': 'core'})):
        name = product.find("div", attrs={'class': 'name'})
        print (name)
        print('No.', index, 'Name:', name.text.upper())

        price = product.find('div', attrs={'class': 'prc'})
        print('      Price:', price.text)
        print(
        "---------------------------------------------------------------------------------------------------------------------------")
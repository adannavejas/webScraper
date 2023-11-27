# from requests import get
from bs4 import BeautifulSoup
import requests


response = requests.get('https://quotes.toscrape.com/')
print(response.status_code) # this status code will tell us if the connection to the site works 

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})


# this is a for loop that concatenates quotes and authors in one line after the webscraping took place in line 46 and 47
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
<<<<<<< HEAD
#testing
=======
 #testing
>>>>>>> master

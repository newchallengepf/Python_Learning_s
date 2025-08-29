
  import requests
  from bs4 import BeautifulSoup
  url = 'http://books.toscrape.com'

  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup.title.text)

  quotes = soup.find_all('span', class_='text')
  for quote in quotes:
    print(quote.text)
  
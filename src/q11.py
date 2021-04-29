import requests
from bs4 import BeautifulSoup

RESULT = requests.get('https://www.imdb.com/list/ls006266261/')
SOUP = BeautifulSoup(RESULT.text, features='html.parser')

LIST_WEB_ITEMS = SOUP.find_all('h3', {'class': 'lister-item-header'})
RESULT_NAME = []
for item in LIST_WEB_ITEMS:
    for name in item.find_all('a'):
        RESULT_NAME.append(name.text)
print(RESULT_NAME)
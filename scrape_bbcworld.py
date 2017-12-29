from bs4 import BeautifulSoup
from requests import get

website = 'http://www.bbc.com/news/world'
source = get(website).text
soup = BeautifulSoup(source, 'lxml')

def get_first_post():
    article = soup.find('div', class_='buzzard-item')
    link = website[0:18] + article.a['href']
    title = article.a.h3.span.text
    return (title,link)

if __name__ == '__main__':
    print(get_first_post())
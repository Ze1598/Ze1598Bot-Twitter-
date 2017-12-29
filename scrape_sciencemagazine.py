#Scrape Science magazine website: only artciles' titles and links

from bs4 import BeautifulSoup
from requests import get

#Website to be scraped
website = 'http://www.sciencemag.org/'
#Then GET a text version of its source code...
source = get(website).text
#For it to be parsed using lxml to create a BeautifulSoup object
soup = BeautifulSoup(source, 'lxml')

def get_first_article():
    article = soup.find('div', class_ = 'hero__content')
    #remove leading spaces from the title
    article_title = article.h2.a.text.strip()
    article_url = website + article.h2.a['href']
    return (article_title, article_url)

if __name__ == '__main__':
    print(get_first_article())
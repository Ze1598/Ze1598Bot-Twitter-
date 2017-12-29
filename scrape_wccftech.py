#Script to scrape wccftech's first featured article's title and URL
#imports
from bs4 import BeautifulSoup
from requests import get

#target website
website = 'https://wccftech.com/'
#make a GET request for the source code
source = get(website).text
#then parse it using lxml
soup = BeautifulSoup(source, 'lxml')

#this function will return a list, where the first item is the title of the "hottest" article's title, \
#and the second item is the article's URL
def get_first_article():
    article = soup.find('a', class_ = 'featured featured-1')
    #return [article's title, article's URL]
    return [article.h2.text, article['href']]

if __name__ == '__main__':
    print(get_first_article())
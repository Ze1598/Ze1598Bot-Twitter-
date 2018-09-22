from bs4 import BeautifulSoup
from requests import get

# Target website
website = 'http://www.bbc.com/news/world'
# Make a GET request for the source code
source = get(website).text
# Then parse it using lxml
soup = BeautifulSoup(source, 'lxml')

def get_first_post():
    '''
    Get the first featured post in bbc.com, specifically,
    bbc.com/news/world.

    Returns
    tuple
        A tuple containing the first featured article's title
        and URL.
    '''

    # Find the wanted information in the HTML
    article = soup.find('div', class_='buzzard-item')

    # Find the article's URL
    link = website[0:18] + article.a['href']

    # Find the article's title
    title = article.a.h3.span.text
    
    return (title, link)

if __name__ == '__main__':
    print(get_first_post())
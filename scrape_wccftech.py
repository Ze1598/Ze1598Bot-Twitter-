#Script to scrape wccftech's first featured article's title and URL
#imports
from bs4 import BeautifulSoup
from requests import get

# Target website
website = 'https://wccftech.com/'
# Make a GET request for the source code
source = get(website).text
# Then parse it using lxml
soup = BeautifulSoup(source, 'lxml')

def get_first_article():
    '''
    Get the first featured post in wccftech.com.

    Returns
    -------
    tuple
        A tuple containing the first featured post's
        title and URL.
    '''

    # Find the wanted information in the HTML
    article = soup.find('a', class_ = 'featured featured-1')

    #return [article's title, article's URL]
    return (article.h2.text, article['href'])

if __name__ == '__main__':
    print(get_first_article())
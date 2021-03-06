# Necessary module imports
from json import dump
from random import choice
# https://beautiful-soup-4.readthedocs.io/en/latest/
from bs4 import BeautifulSoup
# http://docs.python-requests.org/en/master/
from requests import get

def main():
    '''
    Scrape a featured article in a chosen website; that article's
    title and URL are saved to a dictionary, which is then written
    to a .json file.

    Args:
        None
    
    Returns:
        None
    '''
    # Dictionary to hold the article's title and URL
    article_info = {}
    # Possible websites to be scraped
    scrape_options = ['wccftech', 'bbcworld', 'sciencemag']
    # Choose the website
    scrape_choice = choice(scrape_options)
    # If wccftech is chosen
    if scrape_choice == 'wccftech':
        source = get('https://wccftech.com/').text
        soup = BeautifulSoup(source, 'lxml')
        article = soup.find('a', class_ = 'featured featured-1')
        article_info["article_title"] = article.h2.text
        article_info["article_url"] = article['href']

    # If bbcworld is chosen
    elif scrape_choice == 'bbcworld':
        source = get('http://www.bbc.com/news/world').text
        soup = BeautifulSoup(source, 'lxml')
        article = soup.find('div', class_='buzzard-item')
        article_info["article_title"] = article.a.h3.span.text
        article_info["article_url"] = 'http://www.bbc.com' + article.a['href']

    # If science magazine is chosen
    elif scrape_choice == 'sciencemag':
        source = get('http://www.sciencemag.org/').text
        soup = BeautifulSoup(source, 'lxml')
        article = soup.find('div', class_ = 'hero__content')
        article_info["article_title"] = article.h2.a.text.strip()
        article_info["article_url"] = 'http://www.sciencemag.org' + article.h2.a['href']

    # Save 'article_info' in a new .json file
    with open('intermediaryJSON.json','w') as f:
        dump(article_info, f, indent=4)
    
    return


if __name__ == "__main__":
    main()
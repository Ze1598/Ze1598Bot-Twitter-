from io import BytesIO
# http://docs.python-requests.org/en/master/
import requests
# https://pillow.readthedocs.io/en/latest/index.html
from PIL import Image
# https://beautiful-soup-4.readthedocs.io/en/latest/
from bs4 import BeautifulSoup


def download_xkcd():
    '''
    Download the lates comic from xkcd.com.
    
    Parameters
    ----------
    None

    Returns
    -------
    tuple
        A two-item containing the URL to the comic's page
        and the comic's title.
    '''
    
    try:
        # First get the relevant information about the comic
        # Get the JSON about the latest comic
        comic_json = requests.get('https://xkcd.com/info.0.json').json()
        # The latest comic is always found at this URL
        comic_url = 'https://xkcd.com/'
        # The comic title
        comic_title = comic_json['safe_title']
        # The actual comic (image) URL
        img_url = comic_json['img']

        # Now download the image
        # Make a GET request for the image's URL
        img_request = requests.get(img_url)
        # Create an image from the binary data returned by the request
        img = Image.open(BytesIO(img_request.content))
        # Finally save the image
        img.save(f'latest_xkcd.png')

        return (comic_url, comic_title)
    
    except:
        return None

    # The overly complicated way to download the comic
    '''
    # First obtain the image URL and information relative to the comic
    # The URL for the latest comic post
    comic_url = 'https://xkcd.com/'
    # Make a GET request to the page
    page_req = requests.get(comic_url)
    # Make a BeautifulSoup object from the text of the request response
    comic_soup = BeautifulSoup(page_req.text, 'lxml')
    # Locate the relevant information in the HTML
    contents_div = comic_soup.find('div', id='middleContainer').contents
    # Locate the comic title
    comic_title = contents_div[1].text
    # Locate the image URL
    img_url = ':'.join(contents_div[12].split(':')[1:3]).strip()

    # Now download the image
    # Make a GET request for the image's URL
    img_request = requests.get(img_url)
    # Create an image from the binary data returned by the request
    img = Image.open(BytesIO(img_request.content))
    # Now save the image
    img.save(f'latest_xkcd.png')

    return (comic_url, comic_title)
    ''' 

# Execute the function if the file itself is being run
if __name__ == "__main__":
    try:
        download_xkcd()
    except:
        print('Unable to download the latest comic from xkcd.com')
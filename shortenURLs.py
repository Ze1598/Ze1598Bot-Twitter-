import json, requests, shortenURLs_credentials

#Shortens a URL
def shortenUrl(url):
    #API key to make an authenticated request
    apiKey = shortenURLs_credentials.google_URLs_key
    #req_url is composed by:
    #url for a POST request: https://www.googleapis.com/urlshortener/v1/url
    #?key=: query parameter the for the API key
    #apiKey: the key to to be used in the query parameter
    req_url = f'https://www.googleapis.com/urlshortener/v1/url?key={apiKey}'
    #create a dictionary that contains the URL to be expanded (the argument fed to the function)
    data = {'longUrl': url}
    #then convert the dictionary to json
    json_data = json.dumps(data)
    #before making the request, create the headers for the POST request
    headers = {'Content-type': 'application/json'}
    #then finally make the request
    response = requests.post(req_url, data=json_data, headers = headers)
    #return the id value of the request
    return response.json()['id']

#Expands a shortenned URL
def expandUrl(url):
    #API key to make an authenticated request
    apiKey = shortenURLs_credentials.google_URLs_key
    #'req_url' is composed by:
    #url for the GET request: https://www.googleapis.com/urlshortener/v1/url
    #?key=: query parameter for the API key
    #apikey: the key to be used in the query parameter
    #&shortUrl=: a second query parameter to indicate the shortened URL
    #url: the shortened URL
    req_url = f'https://www.googleapis.com/urlshortener/v1/url?key={apiKey}&shortUrl={url}'
    #then create a GET request
    response = requests.get(req_url)
    #return the longUrl of the request
    return response.json()['longUrl']

if __name__ == '__main__':
    print('Your shortened URL is:', shortenUrl('https://ze1598.wixsite.com/zereviews/single-post/2017/11/26/Impressions-Animal-Crossing-Pocket-Camp'))
    print('Your expanded URL is:', expandUrl('https://goo.gl/7ND8FS'))
# Python file with the API key
import shortenURLs_firebase_credentials
import json, requests


#Shortens a URL
def shortenUrl(deep_link):
    '''
    Receive a normal URL as input, to be shortened
    using the Google Firebase API. For the effect,
    a long Dynamic Link is created so that a POST 
    Request can be made.

    Args:
        deep_link: the URL to be shortened.

    Returns:
        str: A string with the shortened, Dynamic Link.
    '''
    # The API key (from a separate file)
    cred = shortenURLs_firebase_credentials.firebase_api_key
    # API endpoint for the POST request
    endpoint = f'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={cred}'

    # Create the Dynamic Link manually
    # The various parameters for the dynamic link URL
    app_code = 'gtu7d'
    ibi = 'com.url.ios'
    # Format a string to contain the dynamic URL
    dyn_url = f'https://{app_code}.app.goo.gl/?link={deep_link}&ibi={ibi}'
    # The request body of the request (create a dictionary to be parsed into JSON)
    data = {'longDynamicLink': dyn_url}
    json_data = json.dumps(data)

    # Dynamic link constructed with parameters
    '''
    # The various parameters for the dynamic link URL
    dynamicLinkDomain = 'gtu7d.app.goo.gl'
    iosBundleId = 'com.url.ios'
    # The request body of the request (create a dictionary to be parsed into JSON)
    # Instead of formating a single string with the dynamic link URL, send the parameters\
    # as a JSON object in the request body
    req_body = {'dynamicLinkInfo': { "dynamicLinkDomain": dynamicLinkDomain, "link": deep_link, "iosInfo": {"iosBundleId": iosBundleId } } }
    # Create the JSON object from the req_body dictionary
    json_data = json.dumps(req_body)
    '''

    # Create the headers for the POST request
    headers = {'Content-type': 'application/json'}
    
    # Then finally make the request
    response = requests.post(endpoint, data=json_data, headers=headers)

    # Return the 'shortLink' value of the request object (after parsing the response to a JSON object)
    return response.json()['shortLink']


if __name__ == '__main__':
    print('Your shortened URL is:', shortenUrl('https://ze1598.wixsite.com/zereviews'))
    print('Your shortened URL is:', shortenUrl('https://wccftech.com/'))
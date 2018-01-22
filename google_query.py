#https://github.com/abenassi/Google-Search-API
#Module to facilitate google queries
from google import google

def googleSearch(query_param):
    #google.search(content_to_search, pages_to_return)
    search_ = google.search(query_param, lang='pt')
    #return (result_description, result_link)
    #Create a try/except clause for when there are problems retrieving search results
    try:
        return (search_[0].name, search_[0].link)
    except:
        return None
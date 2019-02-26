# Module containing the credentials needed for the bot
import Ze1598Bot_credentials as bot_info
# Script I wrote to shorten URLs using Google's Firebase API
import shortenURLs_firebase
# Script I wrote to update the bot's database of posted tweets
import db_script
import os
from time import time
from datetime import datetime
# Library for the Twitter API; built-in random module
# http://tweepy.readthedocs.io/en/v3.5.0/
import tweepy, random

# The starting time of the script (time how long the script takes to run)
start_time = time()

def login():
    '''
    Authenticate the bot into Twitter's API.
    
    Returns
    -------
    api_instance : tweepy.api.API
        An authenticated instance of the Twitter API.
    '''

    # Create variables for each key, secret, token
    consumer_key = bot_info.consumer_key
    consumer_secret = bot_info.consumer_secret
    access_token = bot_info.access_token
    access_token_secret = bot_info.access_token_secret

    # Set up OAuth and integrate with API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api_instance = tweepy.API(auth)

    return api_instance


def gen_tweet_types():
    '''
    Decide what type of tweets will be created.
    
    Returns
    -------
    new_tweet_types : list
        The types of tweets to be created.
    '''

    # List to hold the types of tweets to be created
    new_tweet_types = []

    # Randomly choose two types of tweets to be created
    for i in range(2):

        # List to contain the possible tweets to be created
        tweets_list = ["tweet_Reddit", "tweet_wccftech", "tweet_sciencemag", "tweet_bbcworld", "PYtoJS", "xkcd"]
        # Randomly choose a tweet type
        tweet = random.choice(tweets_list)
        new_tweet_types.append(tweet)

        # Remove the tweet type chosen to avoid duplicate tweets\
        # (unless the chosen type was "tweet_Reddit")
        if tweet != "tweet_Reddit":
            tweets_list.remove(tweet)
    
    return new_tweet_types


def gen_tweets(tweet_types):
    '''
    Create the new tweets.
    
    Parameters
    ----------
    tweet_types : list
        The type of tweets to be created.

    Returns
    -------
    to_tweet : list
        The newly created tweets ready to be posted.
    '''

    # List to hold the generated tweets
    to_tweet = []

    # Loop through the possible tweets, then choose a random one; repeat this twice
    for tweet in tweet_types:

        # In order to not call every module that can be used, simply call the modules needed for the tweet that has been chosen
        
        # Tweet current date and time, including day of the week and AM/PM
        # Currently not in the options 
        if tweet == "tweet_DateTime":
            import get_Time_Date as T_D
            import dayOfTheWeek2019
            new_tweet = f'Date and time update:\n{dayOfTheWeek2019.dayoftheWeek(dayOfTheWeek2019.day, dayOfTheWeek2019.month, dayOfTheWeek2019.year)}\n{T_D.TalkingClock(T_D.time_format)}.'
        
        # Tweet the current hottest post on a specific subreddit
        elif tweet == "tweet_Reddit":
            import getHotNewReddit
            # Choose a subreddit to target
            subred = random.choice(('technology', 'learnpython', 'programming', 'dadjokes'))
            tweet_Reddit_info = getHotNewReddit.HotNew(subred)
            new_tweet = f'Hottest submission in r/{tweet_Reddit_info[0]}: "{tweet_Reddit_info[1]}" which you can read at {shortenURLs_firebase.shortenUrl(tweet_Reddit_info[2])}.'
        
        # Tweet the current first featured article on wccftech
        elif tweet == "tweet_wccftech":
            import scrape_wccftech
            new_tweet = f'The first featured article on @wccftechdotcom \'s website is "{scrape_wccftech.get_first_article()[0]}", which you can read at {shortenURLs_firebase.shortenUrl(scrape_wccftech.get_first_article()[1])}'
        
        # Tweet the current first featured article on Science magazine
        elif tweet == "tweet_sciencemag":
            import scrape_sciencemagazine
            tweet_sciencemag = scrape_sciencemagazine.get_first_article()
            new_tweet = f'@sciencemagazine \'s featured article is "{scrape_sciencemagazine.get_first_article()[0]}", which you can read at {shortenURLs_firebase.shortenUrl(scrape_sciencemagazine.get_first_article()[1])}'
        
        # Tweet the first featured article on BBC World
        elif tweet == "tweet_bbcworld":
            import scrape_bbcworld
            new_tweet = f'The first article on @BBCWorld \'s website is "{scrape_bbcworld.get_first_post()[0]}", which you can read at {shortenURLs_firebase.shortenUrl(scrape_bbcworld.get_first_post()[1])}'
        
        # Tweet the first result for a google query, using a random word from the first tweet in the Bot's timeline
        # Currently not in the options 
        elif tweet == "tweet_googleQuery":
            import google_query
            # Text of the target tweet
            googleQuery_tweet = api_instance.home_timeline()[0]._json["text"]
            # Choose a random word from that tweet to use as the query parameter
            query_word = random.choice(googleQuery_tweet.split()).lower()
            google_result = google_query.googleSearch(query_word)
            # If there were problems retrieving search results, retry with a different 'query_word'
            # Here I am assuming at the second try the problem won't repeat itself
            if google_result == None:
                query_word = random.choice(googleQuery_tweet.split()).lower()
                google_result = google_query.googleSearch(query_word)
            new_tweet = f'The first result on Google for "{query_word}" is "{google_result[0]}...". You can read the rest at the link {shortenURLs_firebase.shortenUrl(google_result[1])}'
        
        # Scrape an article from a website using Python, save the data to a JSON file, then tweet the data using JavaScript
        elif tweet == "PYtoJS":
            # Change directories 
            os.system("cd PYtoJS & python sourcePython.py & node targetJavaScript.js")
            os.system("cd ..")
        
        # Upload the latest xkcd.com comic (tweet an image)
        elif tweet == "xkcd":
            import download_xkcd
            xkcd_comic = download_xkcd.download_xkcd()
            new_tweet = f'Latest @xkcdComic: "{xkcd_comic[1]}", available at {xkcd_comic[0]}'

        # Only save the tweet and append it to the list if it's not a "PYtoJS" type of tweet.\
        # Those are always posted through a JavaScript script
        if tweet != "PYtoJS":
            # Check if the created tweet already exists in the database.
            # Since the URLs included in the tweets are Dynamic Links, even the exact same\
            # long URL won't have the same Dynamic Link twice. Thus, we only save in the database\
            # the text up to the URL in each tweet, so that the URLs are not included in the\
            # saved tweets
            to_send = db_script.update_db(db_script.session, new_tweet.split('http')[0], tweet, datetime.now())
            # Update the list of new tweets with the latest created tweet if the tweet is not a duplicate
            if to_send:
                to_tweet.append(new_tweet)


    print()
    print()

    return to_tweet


def post_tweets(new_tweets, api_instance):
    '''
    Post the new tweets.
    
    Parameters
    ----------
    new_tweets : list
        The new tweets ready to be posted.
    api_instance : tweepy.api.API
        An authenticated instance of the Twitter API.

    Returns
    -------
    None
    '''

    # Tweet out the 2 created tweets
    # Before sending the tweet, create a try/except clause to make sure it\
    # doesn't get caught in errors. If any errors are caught just print a\
    # message "Duplicate tweet."
    for tweet in new_tweets:
    
        print(tweet)
    
        try:

            # If a tweet about the latest xkcd.comic was created, then\
            # we need to use a method to post media
            if 'xkcd' in tweet:
                api_instance.update_with_media('latest_xkcd.png', status=tweet)
                # After posting the tweet, delete the image
                try:
                	os.remove('latest_xkcd.png')
                except:
                	pass

            # If it's any other tweet use the regular method to post a text tweet
            else:
                api_instance.update_status(status=tweet)
            
            print('Your tweet has been sent.')
            print()
            print()
            
        except:
        
            print('Duplicate tweet.')
            print()
            print()
    
    return None

# Run the bot by calling the necessary functions
def main():
	# Login to the Twitter API
	logged_in = login()
	# Choose what types of tweets to create
	new_tweet_types = gen_tweet_types()
	# Create the new tweets
	new_tweets = gen_tweets(new_tweet_types)
	# Post the newly created tweets
	post_tweets(new_tweets, logged_in)

if __name__ == "__main__":
	main()
	print('Bot going to sleep.')
	print('Elapsed time:', int(time()-start_time), 'seconds.')
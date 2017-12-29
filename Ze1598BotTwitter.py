#user-created module containing the credentials needed for the bot
import Ze1598Bot_credentials as bot_info
#Library for the Twitter API; built-in random module; module I created to shorten URLs using Google's URL shortener service
import tweepy, random, shortenURLs

#Create variables for each key, secret, token
consumer_key = bot_info.consumer_key
consumer_secret = bot_info.consumer_secret
access_token = bot_info.access_token
access_token_secret = bot_info.access_token_secret

#Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#List to contains the possible tweets to be created
tweets_list = ["tweet_DateTime", "tweet_Reddit", "tweet_wccftech", "tweet_sciencemag", "tweet_bbcworld"]
#List to contain the 2 tweets to be tweeted out
to_tweet = []

#Loop through the possible tweets, then choose a random one; repeat this twice
for i in range(2):
    #Tweet a random tweet from the different tweets I've created
    tweet = random.choice(tweets_list)
    #In order to not call every module that can be used, simply call the modules needed for the tweet that has been chosen
    #Tweet current date and time, in extense
    if tweet == "tweet_DateTime":
        import get_Time_Date as T_D
        import dayOfTheWeek
        tweet_DateTime = f'Date and time update:\n{dayOfTheWeek.dayoftheWeek(dayOfTheWeek.day, dayOfTheWeek.month, dayOfTheWeek.year)}\n{T_D.TalkingClock(T_D.time_format)}.'
        to_tweet.append(tweet_DateTime)
    #Tweet current internet speeds
    elif tweet == "tweet_TestSpeed":
        import InternetConnection_SpeedPing as ConnectSpeed
        tweet_TestSpeed = f'Current connection speeds\n{ConnectSpeed.ping}\n{ConnectSpeed.download}\n{ConnectSpeed.upload}'
        to_tweet.append(tweet_TestSpeed)
    #Tweet the current hottest post on a specific subreddit
    elif tweet == "tweet_Reddit":
        import getHotNewReddit
        subred = random.choice(('technology', 'learnpython', 'programming'))
        tweet_Reddit_info = getHotNewReddit.HotNew(subred)
        tweet_Reddit = f'Hottest submission in r/{tweet_Reddit_info[0]}: "{tweet_Reddit_info[1]}" which you can read at {shortenURLs.shortenUrl(tweet_Reddit_info[2])}.'
        to_tweet.append(tweet_Reddit)
    #Tweet the current first featured article on wccftech
    elif tweet == "tweet_wccftech":
        import scrape_wccftech
        tweet_wccftech = f'The first featured article on @wccftechdotcom \'s website is "{scrape_wccftech.get_first_article()[0]}", which you can read at {shortenURLs.shortenUrl(scrape_wccftech.get_first_article()[1])}'
        to_tweet.append(tweet_wccftech)
    #Tweet the current first featured article on Science magazine
    elif tweet == "tweet_sciencemag":
        import scrape_sciencemagazine
        tweet_sciencemag = scrape_sciencemagazine.get_first_article()
        tweet_sciencemag = f'@sciencemagazine \'s featured article is "{scrape_sciencemagazine.get_first_article()[0]}", which you can read at {shortenURLs.shortenUrl(scrape_sciencemagazine.get_first_article()[1])}'
        to_tweet.append(tweet_sciencemag)
    #Tweet the first featured article on BBC World
    elif tweet == "tweet_bbcworld":
        import scrape_bbcworld
        tweet_bbcworld = f'The first article on @BBCWorld \'s website is "{scrape_bbcworld.get_first_post()[0]}", which you can read at {shortenURLs.shortenUrl(scrape_bbcworld.get_first_post()[1])}'
        to_tweet.append(tweet_bbcworld)

#Tweet out the 2 created tweets
#Before sending the tweet, create a try/except clause to make sure it doesn't get caught in Duplicate tweets errors
for tweet in to_tweet:
    try:
        api.update_status(status=tweet)
        print('Your tweet has been sent.')
    except:
        print('Duplicate tweet.')
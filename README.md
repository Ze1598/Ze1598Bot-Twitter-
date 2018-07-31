# Ze1598Bot-Twitter-
A Twitter bot created to put scripts I create into practice
The bot was created using Python 3, and right now it does the following:

-Tweet date and time, in text (e.g.: "Date and time update: Today is Friday, December 29th, 2017. It's eleven forty three am.");

-Tweet articles' titles and URLs from various websites (wccftech, sciencemagazine, reddit and bbcworld at the moment);

-All the URLs used in tweets are shortened using the Google URL shortener API;

-For Reddit, it posts the "hottest" post at the moment, its title and shortened URL, from the Technology, Python Education or Programming subreddits;

-It can also post my current Internet speeds (though that option is "disabled" in the code at the moment).

Update logs:

-(june 14th 2018) Deleted the code used to tweet internet speeds due to problems with the module used for that. Also added the possibility to tweet the hottest post in the dadjokes subreddit

-(july 28th 2018) Added a new module (download_xkcd.py) to download and post the latest xkcd.com comic (posted as a media tweet). I also updated the main script structure (Ze1598BotTwitter.py)

-(july 31st 2018) Added a new module (db_script.py) and a SQLite database. This module is responsible for updating the database with new tweets as they are created. Since this database won't contain duplicate tweets it will prevent against posting duplicate tweets.



External references:

-Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

-Requests: http://docs.python-requests.org/en/master/

-praw (The Python Reddit API Wrapper): https://github.com/praw-dev/praw

-pyspeedtest: https://github.com/fopina/pyspeedtest

-Google Search API: https://github.com/abenassi/Google-Search-API

-Tweepy: https://github.com/tweepy/tweepy/tree/920f5c49c059c4ea7f16c7c4f070c484161525c3

-Twitter for node.js: https://github.com/desmondmorris/node-twitter

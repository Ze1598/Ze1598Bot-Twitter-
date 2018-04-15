# Ze1598Bot-Twitter-
A Twitter bot created to put scripts I create into practice
The bot was created using Python 3, and right now it does the following:

-Tweet date and time, in text (e.g.: "Date and time update: Today is Friday, December 29th, 2017. It's eleven forty three am.");

-Tweet articles' titles and URLs from various websites (wccftech, sciencemagazine, reddit and bbcworld at the moment);

-All the URLs used in tweets are shortened using the Google URL shortener API;

-For Reddit, it posts the "hottest" post at the moment, its title and shortened URL, from the Technology, Python Education or Programming subreddits;

-It can also post my current Internet speeds (though that option is "disabled" in the code at the moment).

Update logs:

-(feb. 6th 2018) Now the main script has the option to run the PYtoJS process

-(mar. 30th 2018) Corrected a bug where the URL for the scraped Science Magazine articles wasn't complete; Also removed the Date and Time Update from the possible tweets rotation

-(apr. 15th 2018) Migrated URL shortening from Google URL Shortener to Firebase Dynamic Links; also created a separate file for the update logs of the repo (from now on I will only keep the 3 most recent updates in the README)



External references:

-Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

-Requests: http://docs.python-requests.org/en/master/

-praw (The Python Reddit API Wrapper): https://github.com/praw-dev/praw

-pyspeedtest: https://github.com/fopina/pyspeedtest

-Google Search API: https://github.com/abenassi/Google-Search-API

-Tweepy: https://github.com/tweepy/tweepy/tree/920f5c49c059c4ea7f16c7c4f070c484161525c3

-Twitter for node.js: https://github.com/desmondmorris/node-twitter

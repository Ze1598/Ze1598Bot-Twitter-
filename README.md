# Ze1598Bot-Twitter-
A Twitter bot created to put scripts I create into practice
The bot was created using Python 3, and right now it does the following:

-Tweet date and time, in text (e.g.: "Date and time update: Today is Friday, December 29th, 2017. It's eleven forty three am.");

-Tweet articles' titles and URLs from various websites (wccftech, sciencemagazine, reddit and bbcworld at the moment);

-All the URLs used in tweets are shortened using the Google URL shortener API;

-For Reddit, it posts the "hottest" post at the moment, its title and shortened URL, from the Technology, Python Education or Programming subreddits;

-It can also post my current Internet speeds (though that option is "disabled" in the code at the moment).

Update logs:

-(dec. 30th 2017) Tweet the first result for a google query using a random word from the first tweet in the Bot's feed

-(jan. 1st 2018) Added a new version of dayOfTheWeek.py for 2018, by switch the existing one for dayOfTheWeek2018.py

-(jan. 3rd 2018) Added a try/except clause to the shortenURLs.py file, to prevent exceptions when, for instance, there's problems with the API servers. This way, the script will return the same URL (a long URL) but it won't raise any exceptions

-(jan. 14th. 2018) Updated scrape_sciencemagazine.py with an updated scraped URL

-(jan. 14th 2018) Added a PYtoJS folder: contains scripts in Python and JavaScript, so that it scrapes an article from a given website using Python, saves that information to a .json file and then reads that file and posts a tweet about it using JavaScript. Note: the current intermediaryJSON.json file's content is just an example of what the file may contain.

-(jan 22nd 2018) Added a way to work around cases when the retrieval of google query search results had problems. Now when this happens, the main file simply feeds that script a second word for it to search for (it assumes the problem won't happen with the second word). I also updated a string at the end of PYtoJS/targetJavaScript.js

-(feb. 6th 2018) Now the main script has the option to run the PYtoJS process


External references:

-Google Search API: https://github.com/abenassi/Google-Search-API
-Tweepy: https://github.com/tweepy/tweepy/tree/920f5c49c059c4ea7f16c7c4f070c484161525c3
-Twitter for node.js: https://github.com/desmondmorris/node-twitter

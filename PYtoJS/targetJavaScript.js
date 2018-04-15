//Script to make a Tweet using an article's title and URL scraped using Python

//Import the first .json file with the article's information
const json_file = require('./intermediaryJSON.json');
//Assign the article's information to separate variables
const title = json_file["article_title"];
const articleURL = json_file["article_url"];
// console.log("Article title:", title);
// console.log("Article URL:", articleURL);
// console.log();

//Import the second .json file with the Twitter Bot credentials
const bot_cred = require('./ze1598Bot_credentials.json');
//Import a module to interact with Twitter's API
var Twitter = require('twitter');

//Save the credentials to a new Twtter object
var client = new Twitter({
    consumer_key: bot_cred["consumer_key"],
    consumer_secret: bot_cred["consumer_secret"],
    access_token_key: bot_cred["access_token"],
    access_token_secret: bot_cred["access_token_secret"],
});

//Created the string to be used in tweet
let tweet_text = `\"${title}\", which you can read at ${articleURL}.\n\n***This tweet was \
posted using JavaScript and the article was scraped using Python.***`;
console.log(tweet_text);
console.log();

//Post the tweet
client.post('statuses/update', {status: tweet_text}, function(error, tweet, response){
    // console.log(error);
    // console.log(tweet);
});

//Log a final statement before ending the script
console.log('Your tweet has been sent.');
console.log();
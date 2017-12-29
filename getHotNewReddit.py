#Script to retrieve the top nth submissions of the "hot" and "new" sections of a certain subreddit
#Depending on the section, different attributes will be printed
import praw
#file with credential for the bot
import Ze1598Bot_credentialsReddit as cred
reddit_instance = praw.Reddit(client_id = cred.client_id, client_secret = cred.client_secret, user_agent = cred.user_agent)

def HotNew(subred):
    subreddit_instance = reddit_instance.subreddit(subred)

    #Create a list with the top 'limitsub' submissions in the hot section of 'subreddit_instance'
    first_nth_hot = list(subreddit_instance.hot(limit=3))
    #Then print the title, score and url of each submission
    # return 'Hottest submission in r/{}:\n{}'.format(subred, first_nth_hot[2].title)
    return [subred, first_nth_hot[2].title, first_nth_hot[2].url]


if __name__ == '__main__':
    print(HotNew('technology'))
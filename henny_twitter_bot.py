import tweepy
import config
import random

print('\n\n\n\n\nHENNY TWITTER BOT ACTIVATED\n\n\n\n\n')

# @TheDJHenny tokens
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_KEY = config.ACCESS_KEY
ACCESS_SECRET = config.ACCESS_SECRET

# Twitter authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)



FILE_NAME = 'last_seen_id.txt'

# Methods for updating the last seen tweet to prevent duplicate posts
def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

# Prevents sending too many requests to Twitter's servers
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

last_seen_id = retrieve_last_seen_id(FILE_NAME)


# Create list of tweets
tweet_list = []
tweet_list.append("Follow me for a free bottle of henny! Hit my DMs!")
tweet_list.append("Want a free bottle of henny?? Follow my account and shoot me a DM!")
tweet_list.append("Free bottle of henny to the next 50 people that follow me!")

# Search Twitter for tweets including keyword
results = limit_handled(tweepy.Cursor(api.search,q="#henny",count=10000,
                           lang="en",
                           since_id=last_seen_id,tweet_mode='extended').items())

# Loops through resulting tweets
for result in results:
	

	tweet = random.choice(tweet_list)
	
	#Prints 
	print(result.id)
	print("HENNY BOT INITIATED")

	# Posts resulting tweets and shows what the bot will tweet
	print("@" + result.user.screen_name + ": '" + result.full_text + "'")
	print("@TheDJHenny: '@" + result.user.screen_name + " " + tweet + "'\n")
	
	# Updated last_seen_id to prevent responding to the same tweet
	last_seen_id = result.id
	store_last_seen_id(last_seen_id, FILE_NAME)
	
	# Posts Tweet
	api.update_status('@' + result.user.screen_name + 
							" " + random.choice(tweet_list), result.id)


						
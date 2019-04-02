import tweepy
import random
import keys

print('\n\n\n\n\nHENNY TROLL BOT ACTIVATED\n\n\n\n\n')

"""@TheDJHenny"""
CONSUMER_KEY = 'pG0jjsVnstfvpBCmmGHwoJdGX'
CONSUMER_SECRET = 'QSJbayNasYQIYjCCM79e1OaL5EhsOu7IoNh4b70GyBk9AXMxW1'
ACCESS_KEY = '46678381-QrZvRR2RIoRJVZfYTPEiMHiZ8w7OaQy4w1jn9TUxp'
ACCESS_SECRET = 'ju4GtOOrbYica0bN3ls1h7SuFV2Pks0QYXgBcLIdA9TyQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)



FILE_NAME = 'last_seen_id.txt'

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

last_seen_id = retrieve_last_seen_id(FILE_NAME)


"""Create list of insults"""
shit_talk_list = []
shit_talk_list.append("lol what do you know about henny???")
shit_talk_list.append("I bet you've never had a sip of henny in your life LOL")
shit_talk_list.append("My mom could out drink you hahahaha")
shit_talk_list.append("In Soviet Russia, henny drinks YOU!")
shit_talk_list.append("Sounds like you need a crash course on how to drink henny like a MAN")

"""Search Twitter for tweets including keyword"""
results = api.search(q="#henny",count=10000,
                           lang="en",
                           since_id=2019-31-1)

for result in results:
	"""insult = random.choice(shit_talk_list)"""
	insult = shit_talk_list[0]
	print("HENNY SHIT TALK INITIATED")
	print("@" + result.user.screen_name + ": '" + result.text + "'")
	print("@TheDJHenny: '@" + result.user.screen_name + " " + insult + "'\n")
	"""last_seen_id = result.id"""
	store_last_seen_id(last_seen_id, FILE_NAME)
	"""api.update_status('@' + result.user.screen_name + 
							" " + random.choice(shit_talk_list), result.id)"""


						
import praw 
import urllib.request
import os 

#reddit = praw.Reddit(client_id='voire README', 
	#client_secret='voir README', 
	#user_agent='voir README')

#subreddit = reddit.subreddit('') #ajoute le nom des subreddits sans le r/ et avec des plus pour en mettre plusieurs dans la chaine (string) // add the names of the subreddits without the r/ and with + to add multiple subreddit (one string)
path=os.path.abspath(".")
os.makedirs(path)

with open("\\images\\url.txt", "a") as file:
    print("hello world")
    #for post in subreddit.top(limit=5):
        #if not post.is_self and post.url.endswith(('.jpg', '.jpeg', '.png')):
            #url = post.url
            #file.write(url + '\n')
            #file_name = url.split("/")[-1]
            #urllib.request.urlretrieve(url, "\\images\\" + file_name)
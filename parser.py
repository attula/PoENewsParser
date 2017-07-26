##### Config #####
webhook_url = "https://discordapp.com/api/webhooks/339686063675015170/Sm-I03Vu7Qtfm1xYX2fSNbui0Ck6gRaFSEipoYXye5LgnU4MbKPw4QrykWEdMakDVMoV"
headers = {'Content-Type': 'multipart/form-data'}
feed_url = 'https://www.pathofexile.com/news/rss'

##################

import json
import requests
import feedparser

def send_to_discord(message):
	jsonmsg= '{"content":"'+message + ' "}'
	r = requests.post(webhook_url, data=jsonmsg,verify=False,headers=headers)


def new_news(newlink):
	print(newlink)
	print(oldlink)
	if newlink==oldlink:
		return False
	else: 
		return True

file = open("last.txt","r") 
oldlink=file.read()
file.close()
feed = feedparser.parse(feed_url)

if new_news(feed.entries[0].link):
	message ='@everyone '+ feed.entries[0].link + ' '
	send_to_discord(message)
	file = open("last.txt","w")
	file.write(feed.entries[0].link)
	file.close()
	
else:
	return 0


import urllib2
import json
import codecs

username = 'valgreens'
fi = open("mytweets.txt", "w")
fi.write('My 200 recent tweets: \n\n')
req = urllib2.Request('https://api.twitter.com/1/statuses/user_timeline.json?&include_rts=true&screen_name=' + username +'&count=3200')
opener = urllib2.build_opener()
f = opener.open(req)
tweets = json.load(f) 
contador = 0
for i in tweets:
	fi.write(i['text'].encode('utf-8'))
	fi.write('\n----------\n')
	contador+=1
print contador
fi.close()
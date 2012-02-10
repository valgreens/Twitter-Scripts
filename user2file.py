#!/usr/bin/python
import urllib2
import simplejson as json
import codecs

username = 'valgreens'
url = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=true&screen_name=' + username +'&count=200'

output_file = username + '-tweets.txt'
file_handle = codecs.open(output_file,'w','utf-8')

data = urllib2.urlopen(url).read()
data = json.loads(data)

count = 0

file_handle.write(username + ' 200 recent tweets: \n\n')

for i in data:
	file_handle.write(i['text'] + '\n')
	file_handle.write(i['created_at'] + '\n')
	file_handle.write('----------\n')
	count += 1
	
file_handle.close()
print 'Saved ' + str(count) + ' tweets successfully'
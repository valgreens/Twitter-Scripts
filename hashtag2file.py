#!/usr/bin/python
import urllib2
import simplejson as json
import codecs

hashtag = 'devrefranes'
baseurl = 'http://search.twitter.com/search.json'
query = '?q=%23' + hashtag + '&result_type=recent&rpp=100&show_user=true'
 
output_file = '#' + hashtag + '-tweets.txt'
file_handle = codecs.open(output_file,'w','utf-8')

def getData (query):
	data = urllib2.urlopen(baseurl+query).read()
	data = json.loads(data)
	return data

exit = 0
count = 0

file_handle.write('Tweets from #' + hashtag + ': \n\n')

while (exit == 0):
 	
 	data = getData(query)

	for i in data['results']:
	  file_handle.write('By @' + i['from_user'] + ': ' + i['text'] + '\n')
	  file_handle.write(i['created_at'] + '\n')
	  file_handle.write('----------\n')
	  count += 1
	  
	
	if (data.has_key('next_page')):
		query = data['next_page']
	else:
		exit = 1

file_handle.close()
print 'Saved ' + str(count) + ' tweets successfully'
#/usr/bin/env/python
import json
import urllib
import sys, math

def scrape():
    api_key = 'AIzaSyDjEi6ztheGmbg3wLceacutH0S9twBqULc'
    query = ''
    service_url = 'https://www.googleapis.com/freebase/v1/search'
    newname = "The Godfather" #'"'+actorname+'"'
    params = {
	    'query': query,
	    'limit': 3,
	    
	    #'exact': 'true',
	    #'type': '/film/film',
	    #'pk': '/film/actor',
	    'filter': '(all portrayed_by:"Harrison Ford"  )',
	    #'filter': '(all type:/common/topic/image)',
	    #'output':'type',
	    'key': api_key
    }
    url = service_url + '?' + urllib.urlencode(params)
    movielist = json.loads(urllib.urlopen(url).read())
    print movielist

scrape()

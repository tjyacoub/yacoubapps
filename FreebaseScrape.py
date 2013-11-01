#/usr/bin/env/python
import json
import urllib
import sys, math

mastermoviekey={}
pkF = 1
actorlist = []
for line in open("actorlist.csv"):
    try: 
	line.split()[1]
	l = line.rstrip('\n')
	#l = line.replace('\'','x')
	actorlist.append(l)
    except:
	pass
print actorlist
def scrape(actorname,pkF,last_actor):
    api_key = 'AIzaSyDjEi6ztheGmbg3wLceacutH0S9twBqULc'
    query = ''
    service_url = 'https://www.googleapis.com/freebase/v1/search'
    newname = '"'+actorname+'"'
    params = {
	    'query': query,
	    'limit': 40,
	    
	    #'exact': 'true',
	    #'type': '/film/film',
	    #'pk': '/film/actor',
	    'filter': '(all type:film  contributor:'+newname+' )',
	    #'filter': '(all type:/common/topic/image)',
	    #'output':'type',
	    'key': api_key
    }
    url = service_url + '?' + urllib.urlencode(params)
    movielist = json.loads(urllib.urlopen(url).read())
    print movielist

    actormovielist=[]
    L = len(movielist)
    c=0
    for result in movielist['result']:
    	#title = '"'+result['name']+'"'
	title = result['name']
	#title = title.encode('utf8')
	
	if title not in mastermoviekey:
	    actormovielist.append(pkF)
	    mastermoviekey[title]=pkF

	    t_movie = {}
	    t_movie["model"] = "newapp.Film"
	    t_movie["pk"] = pkF
	    t_movie["fields"] = {}
	    t_movie["fields"]["filmtitle"] = title
	    
	    mastermovies.append(t_movie)
	    pkF += 1
	else: actormovielist.append(mastermoviekey[title]) 
	c += 1
    #print mastermoviekey
    return pkF, actormovielist

def writeactors(actor,movies,pkA,last_actor):

	t_actor = {}
	t_actor["model"] = "newapp.Actor"
	t_actor["pk"] = pkA
	t_actor["fields"] = {}
	t_actor["fields"]["actorname"] = actor
	t_actor["fields"]["movies"] = movies

	return t_actor

pkA = 1
mastermovies = []
masteractors = []
c=0
L=len(actorlist)
last_actor=0
for actor in actorlist:
    if c == L:  last_actor=1 
    if last_actor==1: print "last_actor"
    pkF, actormovielist = scrape(actor,pkF,last_actor)
    masteractors.append(writeactors(actor,actormovielist,pkA,last_actor))
    pkA += 1
    c+=1

moviejson = open("moviedata.json",'w')
data = json.dumps(mastermovies)
moviejson.write(data)
moviejson.close()

actorjson = open("actordata.json",'w')
data = json.dumps(masteractors)
actorjson.write(data)
actorjson.close()

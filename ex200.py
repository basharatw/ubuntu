#Example 200 comment.
#x=34-23
#y="Hello"
#z=3.45
#print x
#if z==3.45 or y=="Hello":
#    x=x+1	
#    print y
#    y=y+" Hello"
#print y
#print z
#print x
#print "-----------------------------"
#x= "Basharat is a good boy"
#y = 23

#print "Country %s %s " %(x,y)
#print "-----------------------------"

#from urllib2 import Request, urlopen, URLError

#request = Request('http://placekitten.com/')
#request = Request('http://twitter.com/basharatw')
#try:
#	response = urlopen(request)
#	kittens = response.read()
#	print kittens[559:1000]
#except URLError, e:
#    print 'No kittez. Got an error code:', e

import requests, json

github_url = "https://api.github.com/user/repos"
data = json.dumps({'name':'III-testThroughAPI', 'description':'II - Doing this through a dynamic API call - some test repo'}) 
r = requests.post(github_url, data, auth=('basharatw', 'Wanisan5425'))

print r.status_code
#print r.json()






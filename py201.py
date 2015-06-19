# API and the rest of the stuff

#Requests is an elegant and simple HTTP library for Python, built for human beings. 
import requests, json, random

#FileName - Pick a radom number 
repoName = "testAPICall%s" % random.randint(1, 100) 
print repoName

#GET
#r = requests.get('https://api.github.com/users/basharatw')
#print r.status_code
#print r.json()
#print r.text

#POST
github_url = "https://api.github.com/user/repos"
data = json.dumps({'name':repoName, 'description': repoName})
r = requests.post(github_url, data, auth=('basharatw', 'Wanisan5425'))
print r.json()
print r.url
print r.encoding
print r.status_code
 
print r.status_code == requests.codes.ok
print r.headers

#r = requests.get('https://api.github.com/events')
#GET
#r = requests.get('https://api.github.com/rate_limit')
#r = requests.get('https://api.github.com/events')
#r = requests.get('https://api.github.com/users/basharatw')
#print r.status_code
#print r.text
#print r.json()

#DELETE




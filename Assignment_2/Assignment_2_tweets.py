import requests
from requests_oauthlib import OAuth1
import os, json
from time import sleep


url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('CJDbbkhUJPCG6UodoypPaZjEQ', 'b2lslDRhlmoNu10fMD3cWtqgjUYLjkWe2DxFe6UuNXg7fkSyNI',
                  '2558496216-SuPVyV3fxLbCUGE8wXEBFV0q3FtXrdjD8Ysz2Vn', 'iqG4hbBxAarxBk52U3zRKYRIwbFq7mQCdxRm1rcx1FmJB')
requests.get(url, auth=auth)

searchterm = input("Please input some word : ")

searchterm = searchterm.replace(" ", "%20")

getTweet = 'https://api.twitter.com/1.1/search/tweets.json?q=%40'+searchterm+'&count=500'
response = requests.get(getTweet, auth = auth)
response = response.json()

path = searchterm.replace("%20"," ").upper()

#if not os.path.exists(path):
#    os.makedirs(path)



#prettyprint = json.dumps(response, indent=4, sort_keys=True)
#print(prettyprint)

with open(path +'.json', 'w') as f:
     json.dump(response, f)

#print(response)

#type(response)

with open(path +'.json', 'r') as readf:
    for line in readf.readlines():
        data = json.loads(line);
    
tweetdata = {}
retweetCount = {}
areatimezone = {}
sorttweets =[]
for statuses in data['statuses']:
    tweetdata[statuses['id']] = statuses
    
for key in tweetdata:
     retweetCount[key] = tweetdata[key]['retweet_count']

sorttweets = sorted(retweetCount.items(), key=lambda x: x[1])
a=[]  
a = sorttweets[-1:]
#print(a)


for id in tweetdata:
    user = tweetdata[id]['user']
    if user['time_zone'] is not None: 
        if user['time_zone'] in areatimezone:
            areatimezone[user['time_zone']] += 1
        else:
            areatimezone[user['time_zone']] = 1
            
sorttimezone = sorted(areatimezone.items(), key=lambda x: x[1])
b = sorttimezone[-10:]

for (p,q) in b:
    print("Tweetcount in ", p +" is ---->", q)

#type(a)
#ype(areatimezone)
#print(b)
#print(tweetdata)



text = []
for (x,y) in a:
    if x in tweetdata:
        text.append(tweetdata[x]['text'])

print("Most retweeted tweet for "+searchterm.replace("%20"," ")+ " is:", text[0])


count = 0
followers_count = 0
for id in tweetdata:
    user = tweetdata[id]['user']
    if user['followers_count'] is not None:
        followers_count += user['followers_count']
        count += 1
        
#print(followers_count)
#print(count)

#avg_followers_count = (int)(followers_count/count)
print("Each user tweeting for "+searchterm.replace("%20"," ")+" has on an average", (int)(followers_count/count) ,"followers. " )

count_friends = 0
friends_count = 0
for id in tweetdata:
    user = tweetdata[id]['user']
    if user['friends_count'] is not None:
        friends_count += user['friends_count']
        count_friends += 1
        
#print(friends_count)
#print(count_friends)

#avg_followers_count = (int)(followers_count/count)
print("Each user tweeting for "+searchterm.replace("%20"," ")+" on an average follows", (int)(friends_count/count_friends) ,"users.")


favoritecount = {}
for key in tweetdata:
     favoritecount[key] = tweetdata[key]['favorite_count']
    
sortfavorites = sorted(favoritecount.items(), key=lambda x: x[1])
c=[]  
c = sortfavorites[-1:]
#print(c)

#print(favoritecount)

text1 = []
for (x1,y1) in c:
    if x1 in tweetdata:
        text1.append(tweetdata[x1]['text'])

print("Most liked tweet for "+searchterm.replace("%20"," ")+ " is:",text1[0])



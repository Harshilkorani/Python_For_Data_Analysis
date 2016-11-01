import requests
from requests_oauthlib import OAuth1
import os, json
from time import sleep


path = 'Badges'
if not os.path.exists(path):
    os.makedirs(path)

for i in range(1,100):        
    url = 'https://api.stackexchange.com/2.2/badges?page='+str(i)+'&pagesize=100&order=desc&sort=name&site=stackoverflow&key=IwwP2VRDlnaZ82DdajaXFQ(('
    response = requests.get(url)
    response = response.json()
    print(response)
    with open('Badges/'+str(i)+'.json', 'w') as f:
         json.dump(response, f)


path1 = 'Questions'
if not os.path.exists(path1):
    os.makedirs(path1)


for i in range(1,301):        
    url1 = 'https://api.stackexchange.com/2.2/questions?page='+str(i)+'&pagesize=100&order=desc&sort=activity&site=stackoverflow&key=IwwP2VRDlnaZ82DdajaXFQ(('
    response1 = requests.get(url1)
    response1 = response1.json()
    sleep(2)
    #print(response1)
    with open('Questions/'+str(i)+'.json', 'w') as f:
         json.dump(response1, f)


json_files_path = "C:/PYTHON/Lecture-06/Questions"

present_dict = {}
cust_segments_dict = {}

json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]
#type(json_files)
#print(json_files)
questions = {}
user_reputation = 0
user = {}
owner ={}
text = []

for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            
            for items in json_dict['items']:
                try:
                     for i in items['tags']:
                            if i == 'java':
                                #print("found")
                                if items['owner']['reputation'] is not None:
                                    user[items['owner']['user_id']] = items['owner']['reputation']
                                    text.append(items['owner']['user_id'])
                                    
                #questions[items['question_id']] = items
                #text.append(questions)
                except KeyError:
                    continue
#newA = dict(sorted(user.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])  

top5 = sorted(user, key=user.get, reverse=True)[:5]
#print(newA)

#import csv
#with open('users.csv', 'w') as csv_file:
    #writer = csv.writer(csv_file)
    #for key, value in user.items():
           #writer.writerow([key, value])
    #writer.writeheader()



json_files_path = "C:/PYTHON/Lecture-06/Users"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]

reputedNames =[]
print("Top 5 Most reputed users for tag Java are as follows:")
for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            #print("Top 5 Most reputed users for Java are as follows:")
            for i in top5:
                for items in json_dict['items']:
                    try:
                        if items['user_id'] is not None:
                            if items['user_id'] == i:  
                                print("User Id" , str(i) +" & Name:", items['display_name'])
                                reputedNames.append(items['display_name'])
                                
                    except KeyError:
                        continue

                        
import csv                        
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error({0}): {1}".format(errno, strerror))    
    return            

csv_columns = ['Row','UserId','Name']
dict_data = [
    {'Row': 1, 'UserId': top5[0], 'Name': reputedNames[0]},
    {'Row': 2, 'UserId': top5[1], 'Name': reputedNames[1]},
    {'Row': 3, 'UserId': top5[2], 'Name': reputedNames[2]},
    {'Row': 4, 'UserId': top5[3], 'Name': reputedNames[3]},
    {'Row': 5, 'UserId': top5[4], 'Name': reputedNames[4]},
    ]

currentPath = os.getcwd()
csv_file = "Top5ReputedUserJava.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)



path2 = 'Privileges'

if not os.path.exists(path2):
    os.makedirs(path2)


    i=1    
    url2 = 'https://api.stackexchange.com/2.2/privileges?page='+str(i)+'&pagesize=100&site=stackoverflow&key=IwwP2VRDlnaZ82DdajaXFQ(('
    response2 = requests.get(url2)
    response2 = response2.json()
    #print(response1)
    with open('Privileges/'+str(i)+'.json', 'w') as f:
         json.dump(response2, f)



path3 = 'Users'
if not os.path.exists(path3):
    os.makedirs(path3)

a = text[2501:4001]
    
count=2500
for i in a:
    count += 1
    user_url = 'https://api.stackexchange.com/2.2/users/'+str(i)+'?site=stackoverflow&key=IwwP2VRDlnaZ82DdajaXFQ(('                 #+'?page='+str(count)+'&pagesize=100&order=desc&sort=reputation&site=stackoverflow&key=IwwP2VRDlnaZ82DdajaXFQ(('
    user_response = requests.get(user_url)
    #sleep()
    user_response = user_response.json()
    #print(response1)
        
    with open('Users/'+str(count)+'.json', 'w') as f:
         json.dump(user_response, f)

#print(user_response)



json_files_path = "C:/PYTHON/Lecture-06/Users"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]
bronze = []
silver = []
gold = []

for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            
            for items in json_dict['items']:
                try:
                    if items['badge_counts']['bronze'] is not None:
                        bronze.append(items['badge_counts']['bronze'])
                    
                    if items['badge_counts']['silver'] is not None:
                        silver.append(items['badge_counts']['silver'])
                        
                    if items['badge_counts']['gold'] is not None:
                        gold.append(items['badge_counts']['gold'])    
                except KeyError:
                    continue
#newA = dict(sorted(user.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])  

#sorted(user, key=user.get, reverse=True)[:5]
#print(newA)
#import csv
#with open('dict.csv', 'wb') as csv_file:
    #writer = csv.writer(csv_file)
    #for key, value in user.items():
           #writer.writerow([key, value])

count_total_number_badges =0       
count_total_bronze_badges = 0
count_total_silver_badges = 0
count_total_gold_badges = 0
for i in bronze:
    count_total_bronze_badges += i
for i in silver:
    count_total_silver_badges += i
for i in gold:
    count_total_gold_badges += i

count_total_number_badges = count_total_bronze_badges + count_total_silver_badges + count_total_gold_badges

#print(count_total_bronze_badges)
#print(count_total_silver_badges)
#print(count_total_gold_badges)
#print(count_total_number_badges)



import csv                        
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error({0}): {1}".format(errno, strerror))    
    return            

csv_columns = ['Row','Badges','Percentage']
dict_data = [
    {'Row': 1, 'Badges': "Gold", 'Percentage': (count_total_gold_badges/count_total_number_badges)*100},
    {'Row': 2, 'Badges': "Silver", 'Percentage': (count_total_silver_badges/count_total_number_badges)*100},
    {'Row': 3, 'Badges': "Bronze", 'Percentage': (count_total_bronze_badges/count_total_number_badges)*100},
    
    ]

currentPath = os.getcwd()
csv_file = "BadgesPercentage.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)





print("Percentage of gold badges   :", (count_total_gold_badges/count_total_number_badges)*100)
print("Percentage of silver badges :", (count_total_silver_badges/count_total_number_badges)*100)
print("Percentage of bronze badges :", (count_total_bronze_badges/count_total_number_badges)*100)



json_files_path = "C:/PYTHON/Lecture-06/Questions"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]
#type(json_files)
#print(json_files)
text = []
privilege_access_site_analytics = 0
privilege_access_moderator_tools = 0
privilege_access_trusted_user = 0
privilege_access_create_chat_rooms = 0
privilege_access_below_100_reputation = 0


for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            
            for items in json_dict['items']:
                try:
                    if items['owner']['reputation'] is not None:
                        user[items['owner']['user_id']] = items['owner']['reputation']
                        text.append(items['owner']['user_id'])
                    
                    if ((items['owner']['reputation']) >= 25000):
                            privilege_access_site_analytics += 1
                    if ((items['owner']['reputation']) >=20000):
                            privilege_access_trusted_user += 1
                    if ((items['owner']['reputation']) >=10000):
                            privilege_access_moderator_tools += 1
                    if ((items['owner']['reputation']) >= 100):
                            privilege_access_create_chat_rooms += 1
                    if ((items['owner']['reputation']) < 100):
                            privilege_access_below_100_reputation += 1
                                    
                #questions[items['question_id']] = items
                #text.append(questions)
                except KeyError:
                    continue

privilege_access_below_100 = (privilege_access_below_100_reputation - 1507)


print((privilege_access_site_analytics/len(text)) *100, "% of users on Stackoverflow.com have access to internal & Google site analytics")
print((privilege_access_trusted_user/len(text)) *100, "% of users on Stackoverflow.com are trusted users who have access to expanded editing, deletion & undeletion privileges")
print((privilege_access_moderator_tools/len(text)) *100, "% of users on Stackoverflow.com have access to moderator tools & can access reports, delete questions & review reviews")
print((privilege_access_create_chat_rooms/len(text)) *100, "% of users on Stackoverflow.com have access to create new chat rooms")
print((privilege_access_below_100/len(text)) *100, "% of users on Stackoverflow.com have reputation less than 100")


import csv                        
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error({0}): {1}".format(errno, strerror))    
    return            

csv_columns = ['Row','Privilege','Percentage']
dict_data = [
    {'Row': 1, 'Privilege': "Access to site Analytics", 'Percentage': (privilege_access_site_analytics/len(text)) *100},
    {'Row': 2, 'Privilege': "Trusted Users", 'Percentage': (privilege_access_trusted_user/len(text)) *100},
    {'Row': 3, 'Privilege': "Access to moderate tools", 'Percentage': (privilege_access_moderator_tools/len(text)) *100},
    {'Row': 4, 'Privilege': "Create New Chat Rooms", 'Percentage': (privilege_access_create_chat_rooms/len(text)) *100},
    {'Row': 5, 'Privilege': "Reputation less than 100", 'Percentage': (privilege_access_below_100/len(text)) *100},
    
    ]

currentPath = os.getcwd()
csv_file = "PrivilegesPercentage.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)





json_files_path = "C:/PYTHON/Lecture-06/Users"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]

age_60_and_above = 0
age_40_and_below_60 = 0
age_30_and_below_40 = 0
age_20_and_below_30 = 0
age_below_20 = 0
people_below_1000_reputation = 0
for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            
            for items in json_dict['items']:
                try:
                    if items['age'] is not None and items['reputation'] is not None:
                        if((items['age']) >= 60 and (items['reputation'] >=1000)):
                            age_60_and_above +=1
                        elif((items['age']) >= 40 and (items['age']) < 60 and (items['reputation'] >=1000)):
                            age_40_and_below_60 +=1
                        elif((items['age']) >= 30 and (items['age']) < 40 and (items['reputation'] >=1000)):
                            age_30_and_below_40 +=1
                        elif((items['age']) >= 20 and (items['age']) < 30 and (items['reputation'] >=1000)):
                            age_20_and_below_30 +=1
                        elif((items['age']) < 20):
                            age_below_20 +=1
                        else:
                            people_below_1000_reputation +=1 
        
                except KeyError:
                    continue
total_people = (age_below_20 + age_20_and_below_30 + age_30_and_below_40 + age_40_and_below_60 + age_60_and_above)                    
#print(people_below_1000_reputation)
print("Percentage of Senior Users using stackoverflow.com & with reputation more than 1000 is :", (age_60_and_above/total_people)*100)
print("Percentage of Very Experienced Users using stackoverflow.com & with reputation more than 1000 is :", (age_40_and_below_60/total_people)*100)
print("Percentage of Experienced Users using stackoverflow.com & with reputation more than 1000 is :", (age_30_and_below_40/total_people)*100)
print("Percentage of Young Users using stackoverflow.com & with reputation more than 1000 is :", (age_20_and_below_30/total_people)*100)
print("Percentage of New & Highly Active Users using stackoverflow.com is :", (age_below_20/total_people)*100)




import csv                        
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error({0}): {1}".format(errno, strerror))    
    return            

csv_columns = ['Row','Age','Percentage']
dict_data = [
    {'Row': 1, 'Age': "Senior Users", 'Percentage': (age_60_and_above/total_people)*100},
    {'Row': 2, 'Age': "Very Experienced Users", 'Percentage': (age_40_and_below_60/total_people)*100},
    {'Row': 3, 'Age': "Experienced Users", 'Percentage': (age_30_and_below_40/total_people)*100},
    {'Row': 4, 'Age': "Young Users", 'Percentage': (age_20_and_below_30/total_people)*100},
    {'Row': 5, 'Age': "New & Highly Active Users", 'Percentage': (age_below_20/total_people)*100},
    
    ]

currentPath = os.getcwd()
csv_file = "AgeGroupPercentage.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)



json_files_path = "C:/PYTHON/Lecture-06/Users"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]

print("Top 5 Most reputed users for tag Java are as follows:")
for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            #print("Top 5 Most reputed users for Java are as follows:")
            for i in top5:
                for items in json_dict['items']:
                    try:
                        if items['user_id'] is not None:
                            if items['user_id'] == i:  
                                print("User Id" , str(i) +" & Name:", items['display_name'])
                    except KeyError:
                        continue
                        

json_files_path = "C:/PYTHON/Lecture-06/Questions"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]
#type(json_files)
#print(json_files)
text = []
top_viewed_questions = {}
for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            
            for items in json_dict['items']:
                try:
                    if items['view_count'] is not None:
                        top_viewed_questions[items['owner']['user_id']] = items['view_count']
                        text.append(items['owner']['user_id'])                     
                #questions[items['question_id']] = items
                #text.append(questions)
                except KeyError:
                    continue
                    
#newA = dict(sorted(user.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])  
#print(top_viewed_questions)
#top10views = sorted(top_viewed_questions, key=top_viewed_questions.get, reverse=True)[:10]

#print(top10views)
#print(newA)
#import csv
#with open('dict.csv', 'wb') as csv_file:
    #writer = csv.writer(csv_file)
    #for key, value in user.items():
           #writer.writerow([key, value])



json_files_path = "C:/PYTHON/Lecture-06/Questions"
json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]
topQuestions = []

print("Top 10 Most viewed questions are as follows:")
for js in json_files:
    full_filename = js.split('.json')
    with open(os.path.join(json_files_path, js)) as one_json_file:
        for line in one_json_file.readlines():
            json_dict = json.loads(line);
            #print(type(json_dict))
            #print("Top 5 Most reputed users for Java are as follows:")
            for i in top10views:
                for items in json_dict['items']:
                    try:
                        if items['owner']['user_id'] is not None:
                            if items['owner']['user_id'] == i:  
                                print("User Id" , str(i) +" & Question:", items['title'])
                                topQuestions.append(items['title'])
                    except KeyError:
                        continue
                        
import csv                        
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error({0}): {1}".format(errno, strerror))    
    return            

csv_columns = ['Row','UserId','Question']
dict_data = [
    {'Row': 1, 'UserId': top10views[0], 'Question': topQuestions[0]},
    {'Row': 2, 'UserId': top10views[1], 'Question': topQuestions[0]},
    {'Row': 3, 'UserId': top10views[2], 'Question': topQuestions[0]},
    {'Row': 4, 'UserId': top10views[3], 'Question': topQuestions[0]},
    {'Row': 5, 'UserId': top10views[4], 'Question': topQuestions[0]},
    {'Row': 6, 'UserId': top10views[5], 'Question': topQuestions[0]},
    {'Row': 7, 'UserId': top10views[6], 'Question': topQuestions[0]},
    {'Row': 8, 'UserId': top10views[7], 'Question': topQuestions[0]},
    {'Row': 9, 'UserId': top10views[8], 'Question': topQuestions[0]},
    {'Row': 10,'UserId': top10views[9], 'Question': topQuestions[0]},
    
    ]

currentPath = os.getcwd()
csv_file = "Top10QuestionsViewed.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)
 
                        



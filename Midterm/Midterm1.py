import requests
from requests_oauthlib import OAuth1
import os, json
from time import sleep


print("ANALYSIS 1:")
json_files_path = "C:/PYTHON/Lecture-06/Questions"

present_dict = {}
cust_segments_dict = {}

json_files = [json_pos for json_pos in os.listdir(json_files_path) if json_pos.endswith('.json')]

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
                      
            for items in json_dict['items']:
                try:
                     for i in items['tags']:
                            if i == 'java':
                                
                                if items['owner']['reputation'] is not None:
                                    user[items['owner']['user_id']] = items['owner']['reputation']
                                    text.append(items['owner']['user_id'])
                                    
                #questions[items['question_id']] = items
                #text.append(questions)
                except KeyError:
                    continue  

top5 = sorted(user, key=user.get, reverse=True)[:5]





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
						
						
						

print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")						
print("ANALYSIS 2:")						
						
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


print("Percentage of gold badges   :", (count_total_gold_badges/count_total_number_badges)*100)
print("Percentage of silver badges :", (count_total_silver_badges/count_total_number_badges)*100)
print("Percentage of bronze badges :", (count_total_bronze_badges/count_total_number_badges)*100)





print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")						
print("ANALYSIS 3:")


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




print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")						
print("ANALYSIS 4:")

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






print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")						
print("ANALYSIS 5:")

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
                    

top10views = sorted(top_viewed_questions, key=top_viewed_questions.get, reverse=True)[:10]




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


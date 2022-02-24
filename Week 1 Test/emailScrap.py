import re
import json
regex = regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def emailScrap(content):
    emails = re.findall(regex, content)
    email_dict = {}
    for email in emails:
        email_dict[email] = {}
        email_dict[email]['Occurance'] = emails.count(email)
        if re.fullmatch('\S+\.\S+@\S+', email):
            email_dict[email]['EmailType'] = 'Human'
        else:
            email_dict[email]['EmailType'] = 'Non-Human'
            
    return email_dict
    

emailScrap("Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedincontacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com")

f = open('websiteData.txt', 'r')
lines = f.readlines()
content = ' '
for word in lines:
    content += ' ' + word
    
email_result = emailScrap(content)
print(email_result)

to_json = open('result.json', 'w')
to_json = json.dump(email_result, to_json)
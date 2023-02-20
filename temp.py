import requests
import json


x = requests.get('https://google.com')
print(dir(x))
print(x.status_code)
# x.encoding = 'utf8'
# t = json.loads(x.content)
# print(t)

'''
Content-Length: 200,
Content-Type: applicaiton/html
Result: 1

'''



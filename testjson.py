import json
dict = {'phoneNum':'17665344887'}
str = json.dumps(dict)
print(dict)
print(str)
dict2 = json.loads(str)
print(dict2)
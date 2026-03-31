import re

text='call to 564-525-6588 right now'

pattern= r'\d\d\d-\d\d\d-\d\d\d\d'


result=re.search(pattern,text)

print(result.group())

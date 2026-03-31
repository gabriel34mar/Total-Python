import re 

text = 'If you need help call (658)-598-9977 for online help'

pattern= 'help'

search=re.search(pattern,text)#Para una
search_all=re.findall(pattern,text)#para encontrr todos 

print(search.start())
print(search.end())
print(search)
print(search_all)

for finding in re.finditer(pattern,text):
    print(finding.span())
    
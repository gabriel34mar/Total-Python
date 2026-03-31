import re

text="Saturday and sunday this store is closed"
search1=re.search(r'.lose',text)
search=re.search(r'sunday|monday',text)
print(search1)
print(search)
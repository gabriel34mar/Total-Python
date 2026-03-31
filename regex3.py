import re 
password = input("Password: ")
pattern =r'\D{1}\w{7}'

check= re.search(pattern,password)

print(check)
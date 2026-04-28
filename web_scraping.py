import bs4 
import requests

result = requests.get("https://www.videoschool.com/")

soup=bs4.BeautifulSoup(result.text,'html.parser')

my_p=soup.select('p')[6].getText()
print(my_p)

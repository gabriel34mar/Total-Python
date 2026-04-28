import bs4 
import requests

basic_url='https://books.toscrape.com/catalogue/page-{}.html'

reslt=requests.get(basic_url.format('1'))

soup=bs4.BeautifulSoup(reslt.text,'html.parser')


books=soup.select('.product_pod')

example=books[0].select('a')[1]['title']

print(example) 
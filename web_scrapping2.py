import bs4
import requests

result = requests.get("https://www.videoschool.com/")
soup = bs4.BeautifulSoup(result.text, 'html.parser')

central_block = soup.select('.fusion-text.fusion-text-1 h1')

for h in central_block:
    print(h.getText())
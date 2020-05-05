from bs4 import BeautifulSoup
import requests
url = 'https://in.investing.com/news/markets/stock-market'
r = requests.get(url,verify=False, headers={'User-Agent': 'PostmannRuntime/7.21.0'})
soup = BeautifulSoup(r.text,'lxml')
# print(soup.prettify())
section = soup.find('ul', {'class': "common-articles-list"})
link = section.li['data-url']
print(link)
# print(section.prettify())
# for content in section.find_all('div', {'class': "content"}):
#     print(content.h3.a.text)

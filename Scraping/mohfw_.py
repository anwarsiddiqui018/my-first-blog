from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.mohfw.gov.in/'
r = requests.get(url,verify=False, headers={'User-Agent': 'PostmannRuntime/7.21.0'})

# print(page)

content = page.content
# print(content)

soup = BeautifulSoup(content, 'lxml')
print(soup)

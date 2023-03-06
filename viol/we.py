import requests
from bs4 import BeautifulSoup as BS 
import pandas as pd


url = "https://rp5.ru/Погода_в_Омске"
r = requests.get(url)
soup = BS(r.text, "html.parser")
temp = soup.find('span', class_="t_0")
print(temp.text)
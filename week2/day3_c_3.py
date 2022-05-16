#pip install bs4
import requests as req
from bs4 import BeautifulSoup
#Beatifulsoup를 이용해서 html태그를 데이터를 가져올수 있음.
#a, img태그 추출
url = 'http://finance.naver.com/marketindex'
res = req.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
#a태크
# links = soup.find_all('a')
#img태크
links = soup.find_all('img')
for i in links:
    # print(i.attrs['href'])
    print(i.attrs['src'])

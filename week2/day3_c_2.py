import urllib.request
url='https://www.naver.com/'
try:
    res= urllib.request.urlopen(url)
    data = res.read()
    text =data.decode('utf-8')
    print(text)
except Exception as e:
    print(str(e))
    print('잘못된 경로')

import urllib.request
url='https://image.bugsm.co.kr/album/images/500/1745/174521.jpg'
savaNm = 'hunt.jpg'
urllib.request.urlretrieve(url,savaNm)
print('저장됨')

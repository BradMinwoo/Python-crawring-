#img or url 정보 둘중에 하나로 저장하는app생성

#1. url 입력+ 수집 버튼 클릭시
#img 경로 출력 + (저정/data/image.....)
#2. 삭제버튼 클릭시 ㄷ저장한 정보 삭제
import os
import shutil
import urllib
from tkinter import *
import requests as req
from bs4 import BeautifulSoup
import urllib.request
class myApp:
    # Beatifulsoup를 이용해서 html태그를 데이터를 가져올수 있음.
    # a, img태그 추출
    url = 'http://finance.naver.com/marketindex'
    msg = req.get(url)
    soup = BeautifulSoup(msg.text, 'html.parser')
    # a태크
    # links = soup.find_all('a')
    # img태크
    print(msg)

    links = soup.find_all('img')
    for i in links:
        # print(i.attrs['href'])
        print(i.attrs['src'])

    def __init__(self, app):
        self.app = app
        self.app.title('title')
        # self.app.geoetry('640400')
        self.app.resizable(False, False)
        self.input = Entry(self.app)  #input받ㄱ
        self.textBox =  Text(self.app, relief=SUNKEN)
        self.input.grid(row=0,column=0)
        self.textBox.grid(row=1, columnspan=100) #100 칸
        self.btn = Button(self.app, text='수집', command=self.fn_search).grid(row=0, column=1)
        self.btnDel = Button(self.app, text='삭제', command=self.fn_del).grid(row=0,column=2)
        # self.btnSave = Button(self.app, text='저장', command=self.fn_save).grid(row=0,column=3)

    def fn_text(self, msg):
        #Call Function after entry input values in textBox
        self.textBox.insert(INSERT, msg+'\n')
    def fn_search(self ):

        msg = self.input.get()
        msg = req.get(msg)
        soup = BeautifulSoup(msg.text, 'html.parser')
        # a태크
        # links = soup.find_all('a')
        # img태크
        links = soup.find_all('img')

        #폴더 생성

        if not os.path.exists('msg'):
            os.makedirs('msg')

        for i in links:
            # print(i.attrs['href'])
            # print(i.attrs['src'])
            msg = i.attrs['src']
            msg.split('/')
            print(msg)
            print(msg.split('/')[-1])

            urllib.request.urlretrieve(msg, os.getcwd()+'/msg/'+ msg.split('/')[-1])
            self.fn_text(msg)

            #파일 생성 저장
            #
            # urllib.request.urlretrieve(msg, ".jpg")
            # print('저장됨. ')


    def fn_del(self):
        # delete all textBox

        # self.textBox.delete('1.0','end')
        shutil.rmtree(os.getcwd()+'/msg')
        print('삭제되었습니다.')

    # def fn_save(self):

app=Tk()
myApp = myApp(app)
app.mainloop()
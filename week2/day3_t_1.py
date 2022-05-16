from tkinter import *
from tkinter import messagebox as alert

#버튼을 클릭했을 했을때 값을 받아 오는 함수 생성
def fn_click():
    name = txt.get()
    alert.showinfo('이름:', name)



app = Tk() #객체 생성
lbl  = Label(app, text='연락처')
lbl.pack()
txt = Entry(app)
txt.pack()
btn = Button(app, text='ok', command=fn_click)
# command 함수와 mapping시켜주는 것
btn.pack()
app.mainloop()


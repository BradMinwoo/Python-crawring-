from tkinter import *
class myApp:
    def __init__(self, app):
        self.app = app
        self.app.title('title')
        # self.app.geoetry('640x400')
        self.app.resizable(False, False)
        self.input = Entry(self.app)  #input받ㄱ
        self.textBox =  Text(self.app, relief=SUNKEN)
        self.input.grid(row=0,column=0)
        self.textBox.grid(row=1, columnspan=100) #100 칸
        self.btn = Button(self.app, text='search', command=self.fn_search).grid(row=0, column=1)
        self.btnDel = Button(self.app, text='Delete', command=self.fn_del).grid(row=0,column=2)
    def fn_text(self, msg):
        #Call Function after entry input values in textBox
        self.textBox.insert(INSERT, msg+'\n')
    def fn_search(self):
        msg = self.input.get()
        self.fn_text(msg)
    def fn_del(self):
        # delete all textBox
        self.textBox.delete('1.0','end')
app=Tk()
myApp = myApp(app)
app.mainloop()
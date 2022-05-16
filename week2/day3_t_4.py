from tkinter import *
app = Tk()

def donotihg():
    filewin = Toplevel(app)
    fileclose  = Button(filewin, text='Do nothing button')
    fileclose.config(command=app.quit)
    fileclose.pack()
def fn_edit():
    print('에디트여')
def fn_saving():
    print('저장이여')
def fn_close():
    app.quit()

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='Open', command=donotihg)
filemenu.add_command(label='Save', command=fn_saving)
filemenu.add_command(label='Close', command=fn_close)
filemenu.add_command(label='Edit', command=editmenu)

filemenu.add_separator()

editmenu.add_command(label='Delete')
filemenu.add_command(label='Exit',command=fn_close)
menubar.add_cascade(label='File', menu=filemenu)
app.config(menu=menubar)
app.mainloop()
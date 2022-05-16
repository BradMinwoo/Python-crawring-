from tkinter import *

#마우스 이벤트
app = Tk()
def fn_click(event):
    print('마우스 위치(프래임내):', event.x, event.y)
    print('마우스 위치(화면):', event.x_root, event.y_root)

#키보드 이벤트
def fn_push(event):
    print('키보드 char:', event.char)
    print('키보드 keycode:', event.keycode)
frame = Frame(app, width=300, height=300)
frame.bind('<Button-1>',fn_click)
frame.bind('<Key>', fn_push)
frame.focus_set()
frame.pack()
app.mainloop()
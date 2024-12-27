from tkinter import *

def setstr(py, ko):
    print(py)
    print(ko)

def clicked():
    degree = eval(et1.get())
    print(degree)
   
win = Tk()

et1 = Entry(win)
et1.grid(row = 2, column = 0, columnspan = 2)

str = ['파이썬', '코틀린'] 
py = Button(win, text=str[0], command = lambda: setstr(str[0]))
ko = Button(win, text=str[1], command = lambda: setstr(str[1]))
py.grid(row = 0, column = 0, padx = 20)
ko.grid(row = 0, column = 1, padx = 20)

win.mainloop()


    
    
    
    

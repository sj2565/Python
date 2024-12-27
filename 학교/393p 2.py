import tkinter as tk
win = tk.Tk()
win.geometry ('300x200')
win.title('GUI Tkinter!')
win.mainloop()

btn = tk.Button(win, text="윈도 종료")
btn.text = '이것도 지원'
btn['text'] = "윈도 종료 한다"
btn['win'] = win.quit



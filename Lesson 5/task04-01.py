from tkinter import *
from tkinter.messagebox import showinfo
import subprocess

def reply():
    s = entry.get()
    text.insert(1.0, s)
    try:
        subprocess.run([s])
    except FileNotFoundError:
        showinfo(title='Warning', message='Такого приложения не найдено!')


window = Tk()

button = Button(window, text='Запустить', command=reply)
entry = Entry(width=100)
text = Text(height=10, wrap=WORD)

entry.pack()
button.pack()
text.pack()

window.mainloop()
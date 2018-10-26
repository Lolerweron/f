from tkinter import *

window = Tk()
window.title('xD')
window.geometry('800x600')

etykieta = Label(window, text='credit card number:')
etykieta.grid(row=0, column=0)
kod = Entry(window, bg="green")
kod.grid(row=1, column=0)
btn = Button(window, text="click to get free V-Bucks!!!")
btn.grid(row=1, column=1)
def kradnijkarte():
    etykieta.configure(text=kod.get())
btn.configure(command=kradnijkarte)
window.mainloop()


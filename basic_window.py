import tkinter as tk 
from tkinter import ttk

def button_func():
    print("lamaw")
    
def print_Hello():
    print("Hello")



#Creation of window
window =tk.Tk()
window.title('Lamaw')
window.geometry('800x500')

#ttk widgets label
label = ttk.Label(master=window, text='this is test')
label.pack()


#tk text 
text = tk.Text(master=window)
text.pack()



#ttk entry
entry = ttk.Entry(master=window,)
entry.pack()

#ttk 
button = ttk.Button(master=window, text= 'press me', command= button_func)
button.pack()

excercise_Label = ttk.Label(master=window, text = 'lamaw')
excercise_Label.pack()

entry_Second = ttk.Entry(master=window, text= 'add text')
entry_Second.pack()

button_Second = ttk.Button(master=window, text='Print hello', command = lambda: print('Hello'))
button_Second.pack()











#run
window.mainloop()

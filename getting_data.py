import tkinter as tk
from tkinter import ttk 

#window
window = tk.Tk()
window.title = "lamaw"


def button_func():
    #Get the content of the entry
    entry_value = entry.get()
    
    label['text'] = entry_value
    entry['state'] = 'disabled'
    
def reset_func():
    label["text"] = 'LIKE'
    entry["state"] = 'enabled'

#widgets
label = ttk.Label(master = window, text = "Hello World")
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(master = window, text = "Press Me", command = button_func)
button.pack()

# ------------------------------------------------------------------------------ #


button_2 = ttk.Button(master = window, text = "PRESS ME TO ENABLE", command = reset_func)
button_2.pack()



window.mainloop()
import tkinter as tk 
#from tkinter import ttk 
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename= 'cyborg')
window.title("Lamaw")
window.geometry("300x150")



def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)





#tittle
tittle_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Minecraft 24')
tittle_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
#This entry varabiables will take every input and store it inside the entryInt variable so we can use it as value for any computations
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command = convert)

#Pack() - is the easiest Layout Manager to code with in Tkinter. Instead of declaring the precise location of a widget, 
#the pack() method declares the position of widgets in relation to each other.

entry.pack(side='left', padx =10)
button.pack(side = "left" )
input_frame.pack(pady=10)


#output 
output_string = tk.StringVar()

output_label = ttk.Label(
    master = window, 
text='output', 
font= 'Minecraft 24', 
textvariable=output_string)

output_label.pack(pady=10)


#function

#run
window.mainloop()
from tkinter import *
from tkinter import ttk 



#window 
window = Tk()
window.title('Buttons')
window.geometry('600x400')

def button_funct():
    print('Basic Function')
    print(radio_var.get()) 

#widgets
#button
button_str = StringVar(value = 'A value with string values')
button_1 = Button(window, text = 'Press ME', command = button_funct, textvariable = button_str)
button_1.pack()

#checkbutton
check_var = IntVar()
check_1 = Checkbutton(window, text = 'Checkbox', 
                      command = lambda: print(check_var.get())
                      , 
                      variable = check_var,
                      onvalue = 10,
                      offvalue = 5)
check_1.pack()

check_2  = Checkbutton(window, 
                       text = 'Checkbox 2',
                       command= lambda: check_var.set(5))
check_2.pack()

#Radio buttons
radio_var = StringVar()
radio_1 = Radiobutton(window, 
                      text = 'Rad but 1', 
                      value = 1,
                      variable = radio_var,
                      command= lambda: print(radio_var.get()))
radio_1.pack()


radio_2 = Radiobutton(window, text = 'Rad but 2', value = 1, variable = radio_var)
radio_2.pack()


#excercise

def radio_func():
    print(check_bool.get())
    check_bool.set(False)
    

radio_str = StringVar()

check_bool = BooleanVar()



exercise_radio1 = Radiobutton(window, text = 'Rad A' , 
                              command = radio_func, 
                              variable = radio_str)


exercise_radio2 = Radiobutton(window, 
                              text = 'Rad B', 
                              command = radio_func, 
                              variable = radio_str)

exercise_check = Checkbutton(window, 
                             text = 'Check', 
                             variable = check_bool, command = lambda:print(radio_str.get()))


#layout
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()








#main loop
window.mainloop()
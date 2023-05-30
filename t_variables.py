from tkinter import *
from tkinter import messagebox

def compute_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())/100
    bmi = weight / (height * height)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI CALCULATOR', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI CALCULATOR', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI CALCULATOR', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI CALCULATOR', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('BMI CALCULATOR', 'something went wrong!')   
    
#window
window = Tk()
window.title('BMI CALCULATOR')
window.geometry('300x150')

#widgets

label_1_weight = Label(window, text = 'Enter weight')
label_1_weight.pack()


weight_entry = Entry(window)
weight_entry.pack()

label_2_height = Label(window, text = 'Enter Height')
label_2_height.pack()

height_entry = Entry(window)
height_entry.pack()

bmi_label = Label(window, text = 'BMI')
bmi_label.pack()

compute_but = Button(window, text = 'Compute', command = compute_bmi)
compute_but.pack()


#Mainloop to run
window.mainloop()


from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady= 20)
window.minsize(width=200, height= 100)

#Create entry 

input = Entry(width=10)
input.grid(column=2, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=2)

#Result

label = Label(text="is equal to")
label.grid(column=1, row = 3)

km_label = Label(text="Km")
km_label.grid(column=3, row=3)

result_label = Label(text="0")
result_label.grid(column=2, row=3)

#Button

def mile_converter():
    result_label["text"] = int(input.get()) * 1.6

button = Button(text="Calculate", command= mile_converter)
button.grid(column=2, row = 4)

window.mainloop()
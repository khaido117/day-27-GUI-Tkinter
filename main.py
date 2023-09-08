from tkinter import *

window =Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx= 20, pady=20)

#Label

my_label =Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column= 0, row= 0)
my_label["text"] = "New Text"
my_label.config(text = "New Text")

#Entry

input = Entry(width="10")
# input.pack()
input.get()
input.grid(column=4, row=3)

#Create button 

def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click here", command=button_clicked)

# button.pack()
button.grid(column=2, row=2)

new_button = Button(text= "New Button")
new_button.grid(column=3, row=0)


window.mainloop()
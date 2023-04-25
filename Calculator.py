from tkinter import *

#simple calculator using tkinter
root = Tk()
root.title("Calculator")


#sizes window exactly to fit everything in it
Grid.rowconfigure(root, (0, 1, 2, 3, 4, 5), weight=1)
Grid.columnconfigure(root, (0, 1, 2, 3), weight=1)

#fixes windowsize
root.resizable(0, 0)

#add all numbers and +, - ... symbols on a string
def button_add(number):
    temp_text = textwindow.get()
    textwindow.delete(0, END)
    textwindow.insert(0, str(temp_text) + str(number))

#once you press = you will see the result
def results():
    temp = textwindow.get()
    temp_result = eval(temp)
    textwindow.delete(0, END)
    textwindow.insert(0, str(temp_result))

#basicaly clear the text window
def delete():
    textwindow.delete(0, END)

#function as to not allow double operatiors(for example ++ or +/) and 
#to also not allow to start with one   
def check(character):
    temp_text = textwindow.get()
    if((len(temp_text)> 0)):
        if((temp_text[-1] != "+") and (temp_text[-1] != "-") and (temp_text[-1] != "/") and (temp_text[-1] != "*") and (temp_text[-1] != "**") and (temp_text[-1] != ".")):
            button_add(character)

#funtion to delete last number/operator           
def back():
    temp_text = textwindow.get()
    textwindow.delete(0, END)
    textwindow.insert(0, str(temp_text[:-1]))

#creating the text box to show results and what numbers we haveee chosen so far
textwindow = Entry(root, width= 35, borderwidth= 5)
textwindow.grid(row=0, column=0, columnspan=4, padx= 25, pady=20, sticky='nsew' )

#all the buttons we will be using on the GUI
Button1 = Button(root, text = "1", padx= 40, pady=20, command= lambda: button_add(1))
Button2 = Button(root, text = "2", padx= 40, pady=20, command= lambda: button_add(2))
Button3 = Button(root, text = "3", padx= 40, pady=20, command= lambda: button_add(3))
Button4 = Button(root, text = "4", padx= 40, pady=20, command= lambda: button_add(4))
Button5 = Button(root, text = "5", padx= 40, pady=20, command= lambda: button_add(5))
Button6 = Button(root, text = "6", padx= 40, pady=20, command= lambda: button_add(6))
Button7 = Button(root, text = "7", padx= 40, pady=20, command= lambda: button_add(7))
Button8 = Button(root, text = "8", padx= 40, pady=20, command= lambda: button_add(8))
Button9 = Button(root, text = "9", padx= 40, pady=20, command= lambda: button_add(9))
Button0 = Button(root, text = "0", padx= 40, pady=20, command= lambda: button_add(0))
ButtonDot = Button(root, text = ".", padx= 40, pady=20, command= lambda: check("."))
ButtonAdd = Button(root, text = "+", padx= 40, pady=20, command= lambda: check("+"))
ButtonSub = Button(root, text = "-", padx= 40, pady=20, command= lambda: check("-"))
ButtonDiv = Button(root, text = "/", padx= 40, pady=20, command= lambda: check("/"))
ButtonMul = Button(root, text = "*", padx= 40, pady=20, command= lambda: check("*"))
ButtonPow = Button(root, text = "**",padx= 84, pady=20, command= lambda: check("**"))
ButtonEq = Button(root, text = "=", padx= 40, pady=20, command= lambda: results())
ButtonClear = Button(root, text = "Clear", padx= 29, pady=20, command= lambda: delete())
ButtonBack = Button(root, text = "<==", padx= 30, pady=20, command= lambda: back())

#revealing the buttons on the GUI
Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)
Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)
Button0.grid(row=4, column=0)
ButtonDot.grid(row=4, column=1)
ButtonAdd.grid(row=5, column=2)
ButtonSub.grid(row=5, column=3)
ButtonDiv.grid(row=4, column=3)
ButtonMul.grid(row=3, column=3)
ButtonEq.grid(row=4, column=2)
ButtonClear.grid(row=1, column=3)
ButtonPow.grid(row=5, column=0, columnspan= 2)
ButtonBack.grid(row=2, column=3)

root.mainloop()

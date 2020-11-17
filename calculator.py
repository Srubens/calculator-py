from tkinter import *

window = Tk()
window.title("Calculator")

i = 0

#ENTRADA DE TEXTO 
text_entry = Entry(window, font= ("Montserrat 20"))
text_entry.grid(row= 0, column= 0, columnspan= 4, padx= 5, pady= 5)

def click_btn(value):
    global i
    text_entry.insert(i, value)
    i += 1

def remove():
    text_entry.delete(0, END)
    i = 0 

def operation():
    equation = text_entry.get()
    result = eval(equation)
    text_entry.delete(0, END)
    text_entry.insert(0, result)
    i = 0

#BOTOES
btn1 = Button(window, text="1", width=5, height=2, command = lambda: click_btn(1))
btn2 = Button(window, text="2", width= 5, height=2, command = lambda: click_btn(2))
btn3 = Button(window, text="3", width= 5, height=2, command = lambda: click_btn(3))
btn4 = Button(window, text="4", width= 5, height=2, command = lambda: click_btn(4))
btn5 = Button(window, text="5", width= 5, height=2, command = lambda: click_btn(5))
btn6 = Button(window, text="6", width= 5, height=2, command = lambda: click_btn(6))
btn7 = Button(window, text="7", width= 5, height=2, command = lambda: click_btn(7))
btn8 = Button(window, text="8", width= 5, height=2, command = lambda: click_btn(8))
btn9 = Button(window, text="9", width= 5, height=2, command = lambda: click_btn(9))
btn0 = Button(window, text="0", width= 18, height=2, command = lambda: click_btn(0))

btn_AC = Button(window, text="AC", width=5, height=2, command=lambda: remove())
btn_KinshipOne = Button(window, text="(", width=5, height=2, command = lambda: click_btn("("))
btn_KinshipTwo = Button(window, text=")", width=5, height=2, command = lambda: click_btn(")"))
btn_Point = Button(window, text=".", width=5, height=2, command = lambda: click_btn("."))

btn_Division = Button(window, text="/", width=5, height=2, command = lambda: click_btn("/"))
btn_Multiplication = Button(window, text="*", width=5, height=2, command = lambda: click_btn("*"))
btn_Subtraction = Button(window, text="-", width=5, height=2, command = lambda: click_btn("-"))
btn_Add = Button(window, text="+", width=5, height=2, command = lambda: click_btn("+"))
btn_SameAs = Button(window, text="=", width=5, height=2, command = lambda: operation())

btn_AC.grid(row= 1, column= 0, padx= 5, pady=5)
btn_KinshipOne.grid(row=1,column=1,padx=5,pady=5)
btn_KinshipTwo.grid(row=1,column=2,padx=5,pady=5)
btn_Division.grid(row=1,column=3,padx=5,pady=5)

btn7.grid(row=2,column=0,padx=5,pady=5)
btn8.grid(row=2,column=1,padx=5,pady=5)
btn9.grid(row=2,column=2,padx=5,pady=5)
btn_Subtraction.grid(row=2,column=3,padx=5,pady=5)

btn4.grid(row=3, column=0, padx=5, pady=5)
btn5.grid(row=3, column=1, padx=5, pady=5)
btn6.grid(row=3, column=2, padx=5, pady=5)
btn_Multiplication.grid(row=3, column=3, padx=5, pady=5)

btn1.grid(row=4, column=0, padx=5, pady=5)
btn2.grid(row=4, column=1, padx=5, pady=5)
btn3.grid(row=4, column=2, padx=5, pady=5)
btn_Add.grid(row=4, column=3, padx=5, pady=5)

btn0.grid(row= 5, column= 0, columnspan= 2,padx= 5, pady= 5)
btn_SameAs.grid(row=5, column=2, padx=5, pady=5)
btn_Point.grid(row=5, column=3, padx=5, pady=5)

window.mainloop()

from tkinter import *


app = Tk()
app.title("Calculator")
app.geometry("300x400")
app.resizable(False, False)


expression = ""
input_text = StringVar()

entry = Entry(app, textvariable=input_text, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)


def press(num):
    global expression
    expression = expression + str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

row = 1
col = 0

for b in buttons:
    if b == "=":
        Button(app, text=b, width=5, height=2, font=("Arial",15), command=equal).grid(row=row, column=col)
    else:
        Button(app, text=b, width=5, height=2, font=("Arial",15), command=lambda x=b: press(x)).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

Button(app, text="C", width=22, height=2, font=("Arial",15), command=clear).grid(row=row, column=0, columnspan=4)

app.mainloop()

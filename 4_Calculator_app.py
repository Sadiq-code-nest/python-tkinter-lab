import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

def update_screen(value):
    global expression
    expression += str(value)
    input_var.set(expression)

def clear():
    global expression
    expression = ""
    input_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_var.set(result)
        expression = result
    except:
        input_var.set("Error")
        expression = ""

input_var = tk.StringVar()

screen = tk.Entry(root, textvariable=input_var, font=("Arial", 20), bd=10, relief=tk.SUNKEN, justify="right")
screen.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "C":
        cmd = clear
    elif text == "=":
        cmd = calculate
    else:
        cmd = lambda x=text: update_screen(x)

    tk.Button(frame, text=text, width=6, height=2, font=("Arial", 12), command=cmd).grid(row=row, column=col)

back_btn = tk.Button(root, text="Backspace", command=backspace)
back_btn.pack(fill="x", padx=10, pady=5)

root.mainloop()
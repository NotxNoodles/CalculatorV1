import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y






def on_click(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if operation == 'add':
        result.set(add(num1, num2))
    elif operation == 'subtract':
        result.set(subtract(num1, num2))
    elif operation == 'multiply':
        result.set(multiply(num1, num2))
    elif operation == 'divide':
        result.set(divide(num1, num2))

app = tk.Tk()
app.title("Calculator")

entry1 = tk.Entry(app)
entry1.pack()
entry2 = tk.Entry(app)
entry2.pack()

result = tk.StringVar()
tk.Label(app, textvariable=result).pack()

tk.Button(app, text="Add", command=lambda: on_click('add')).pack()
tk.Button(app, text="Subtract", command=lambda: on_click('subtract')).pack()
tk.Button(app, text="Multiply", command=lambda: on_click('multiply')).pack()
tk.Button(app, text="Divide", command=lambda: on_click('divide')).pack()

app.mainloop()

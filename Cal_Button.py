import tkinter as tk

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"Result = {num1 + num2}")

def sub():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"Result = {num1 - num2}")

def mul():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"Result = {num1 * num2}")

def div():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if num2 == 0:
        result_label.config(text="Cannot divide by zero")
    else:
        result_label.config(text=f"Result = {num1 / num2}")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="+", command=add).pack()
tk.Button(root, text="-", command=sub).pack()
tk.Button(root, text="*", command=mul).pack()
tk.Button(root, text="/", command=div).pack()

result_label = tk.Label(root, text="Result = ")
result_label.pack(pady=10)

root.mainloop()

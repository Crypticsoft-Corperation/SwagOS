import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def perform_operation(operation):
    num1 = simpledialog.askfloat("Input", "Enter the first number:")
    num2 = simpledialog.askfloat("Input", "Enter the second number:")
    if num1 is not None and num2 is not None:
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        messagebox.showinfo("Result", f"The result is {result}")

def main():
    window = tk.Tk()
    window.title("Calculator")

    add_button = tk.Button(window, text="Addition (+)", command=lambda: perform_operation('add'))
    add_button.grid(row=0, column=0, sticky='nsew')

    subtract_button = tk.Button(window, text="Subtraction (-)", command=lambda: perform_operation('subtract'))
    subtract_button.grid(row=1, column=0, sticky='nsew')

    multiply_button = tk.Button(window, text="Multiplication (*)", command=lambda: perform_operation('multiply'))
    multiply_button.grid(row=2, column=0, sticky='nsew')

    divide_button = tk.Button(window, text="Division (/)", command=lambda: perform_operation('divide'))
    divide_button.grid(row=3, column=0, sticky='nsew')

    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.grid(row=4, column=0, sticky='nsew')

    # Configure the rows and columns to expand with the window
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()

if __name__ == "__main__":
    main()

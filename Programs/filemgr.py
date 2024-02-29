import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def display_menu():
    print("Simple File Manager App")
    print("1. List files in the current directory")
    print("2. Create a new file")
    print("3. View file content")
    print("4. Delete a file")
    print("5. Exit")

def list_files():
    files = os.listdir()
    messagebox.showinfo("Files in the current directory", "\n".join(files))

def create_file():
    filename = simpledialog.askstring("Input", "Enter the name of the new file:")
    if filename:
        try:
            with open(filename, 'w') as file:
                messagebox.showinfo("Success", f"File '{filename}' created successfully.")
        except IOError as e:
            messagebox.showerror("Error", f"Error creating file: {e}")

def view_file():
    file_path = simpledialog.askstring("Input", "Enter the full path of the file to view:")
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                messagebox.showinfo(f"Content of '{file_path}'", content)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{file_path}' not found.")
        except PermissionError:
            messagebox.showerror("Error", f"Permission denied. Unable to view '{file_path}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {e}")

def delete_file():
    filename = simpledialog.askstring("Input", "Enter the name of the file to delete:")
    if filename:
        try:
            os.remove(filename)
            messagebox.showinfo("Success", f"File '{filename}' deleted successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{filename}' not found.")
        except PermissionError:
            messagebox.showerror("Error", f"Permission denied. Unable to delete '{filename}'.")

def main():
    window = tk.Tk()
    window.title("Simple File Manager App")

    list_button = tk.Button(window, text="List files in the current directory", command=list_files)
    list_button.grid(row=0, column=0, sticky='nsew')

    create_button = tk.Button(window, text="Create a new file", command=create_file)
    create_button.grid(row=1, column=0, sticky='nsew')

    view_button = tk.Button(window, text="View file content", command=view_file)
    view_button.grid(row=2, column=0, sticky='nsew')

    delete_button = tk.Button(window, text="Delete a file", command=delete_file)
    delete_button.grid(row=3, column=0, sticky='nsew')

    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.grid(row=4, column=0, sticky='nsew')

    # Configure the rows and columns to expand with the window
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()

if __name__ == "__main__":
    main()

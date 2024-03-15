import os
import platform
import tkinter as tk
from tkinter import messagebox

def list_files():
    files = os.listdir()
    result_text.config(state=tk.NORMAL)
    result_text.insert(tk.END, "\n".join(files) + "\n")
    result_text.config(state=tk.DISABLED)

def echo(text):
    result_text.config(state=tk.NORMAL)
    result_text.insert(tk.END, text + "\n")
    result_text.config(state=tk.DISABLED)

def display_sysinfo():
    system_info = platform.uname()
    info = f"""
    System Information:
    System: {system_info.system}
    Node Name: {system_info.node}
    Release: {system_info.release}
    Version: {system_info.version}
    Machine: {system_info.machine}
    Processor: {system_info.processor}
    SwagOS Version: 2.0
    Python Version: 3.12.2
    """
    result_text.config(state=tk.NORMAL)
    result_text.insert(tk.END, info + "\n")
    result_text.config(state=tk.DISABLED)

def process_command(event):
    command = command_entry.get()
    if command == "list_files":
        list_files()
    elif command.startswith("echo "):
        text = command[5:]
        echo(text)
    elif command == "display_sysinfo":
        display_sysinfo()
    else:
        result_text.config(state=tk.NORMAL)
        result_text.insert(tk.END, "Command not recognized\n")
        result_text.config(state=tk.DISABLED)
    command_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Terminal")
window.configure(bg='black')

command_entry = tk.Entry(window, bg='black', fg='white')
command_entry.bind("<Return>", process_command)
command_entry.pack()

result_text = tk.Text(window, bg='black', fg='white', wrap=tk.WORD, state=tk.DISABLED)
result_text.pack()

window.mainloop()
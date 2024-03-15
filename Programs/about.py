import tkinter as tk
from tkinter import messagebox

def about_program():
    info = """Crypticsoft SwagOS
Version 2.0
Python 3.12.2
Copyright 2022-2024 Crypticsoft Corporation. All rights reserved.
    """
    messagebox.showinfo("About SwagOS", info)

def main():
    about_program()

if __name__ == "__main__":
    main()
import tkinter as tk
from datetime import datetime
import subprocess
from tkinter import messagebox
import os
import glob

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

def switch_to_script(script_path):
    try:
        subprocess.Popen(['python', script_path])
    except Exception as e:
        messagebox.showerror("Error", f"Error executing {script_path}: {str(e)}")

def main():
    window = tk.Tk()
    window.title("Crypticsoft SwagOS 2.0")
    window.geometry("640x480")

    # Set desktop background
    window.configure(background='lightblue')

    # Create a frame for the main content
    content_frame = tk.Frame(window, background='lightblue')
    content_frame.pack(expand=True, fill='both')

    label = tk.Label(content_frame, text=f"Current date and time: {formatted_datetime}", background='lightblue')
    label.pack()

    # Create a frame for the Program Manager window and add outline
    program_manager_window = tk.Frame(window, background='gray', width=200, height=400, relief='raised', borderwidth=2)
    program_manager_window.place(relx=0.5, rely=0.5, anchor='center')

    # Add icons for the scripts in the Program Manager window arranged in a grid
    scripts = glob.glob('Programs/*.py')
    for i, script_path in enumerate(scripts):
        script_name = os.path.basename(script_path)
        icon_label = tk.Label(program_manager_window, text=script_name, bg='lightgray', relief='raised', padx=5, pady=5)
        icon_label.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        icon_label.bind("<Button-1>", lambda event, sp=script_path: switch_to_script(sp))

    window.mainloop()

if __name__ == "__main__":
    main()
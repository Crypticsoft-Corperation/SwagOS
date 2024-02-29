import datetime
import calendar
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def view_events(calendar):
    date = simpledialog.askstring("Input", "Enter the date (YYYY-MM-DD):")
    if date in calendar:
        events = calendar[date]
        messagebox.showinfo(f"Events for {date}", "\n".join(events))
    else:
        messagebox.showinfo("Info", f"No events found for {date}.")

def add_event(calendar):
    date = simpledialog.askstring("Input", "Enter the date (YYYY-MM-DD):")
    event = simpledialog.askstring("Input", "Enter the event:")
    if date and event:
        if date in calendar:
            calendar[date].append(event)
        else:
            calendar[date] = [event]
        messagebox.showinfo("Success", f"Event added for {date}.")

def remove_event(calendar):
    date = simpledialog.askstring("Input", "Enter the date (YYYY-MM-DD):")
    if date in calendar:
        events = calendar[date]
        event = simpledialog.askstring("Input", f"Enter the event to remove:\n" + "\n".join(events))
        if event in events:
            events.remove(event)
            messagebox.showinfo("Success", f"Removed event: {event}")
        else:
            messagebox.showerror("Error", "Invalid event. No event removed.")
    else:
        messagebox.showinfo("Info", f"No events found for {date}.")

def main():
    window = tk.Tk()
    window.title("Calendar")

    calendar = {}

    view_button = tk.Button(window, text="View events for a day", command=lambda: view_events(calendar))
    view_button.grid(row=0, column=0, sticky='nsew')

    add_button = tk.Button(window, text="Add an event for a day", command=lambda: add_event(calendar))
    add_button.grid(row=1, column=0, sticky='nsew')

    remove_button = tk.Button(window, text="Remove an event for a day", command=lambda: remove_event(calendar))
    remove_button.grid(row=2, column=0, sticky='nsew')

    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.grid(row=3, column=0, sticky='nsew')

    # Configure the rows and columns to expand with the window
    for i in range(4):
        window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()

if __name__ == "__main__":
    main()

from datetime import datetime
import subprocess

# Get the current time
current_time = datetime.now().time()

# Format the time and print it
formatted_time = current_time.strftime("%H:%M")
print("Crypticsoft SwagOS 1.1")
print("Current time is:", formatted_time)

def display_menu():
    print("1. filemgr.py")
    print("2. cmd.py")
    print("3. about.py")
    print("4. calc.py")
    print("5. calendar.py")
    print("6. Exit")

def switch_to_filemgr():
    script_path = 'filemgr.py'
    switch_to_script(script_path)

def switch_to_cmd():
    script_path = 'cmd.py'
    switch_to_script(script_path)

def switch_to_about():
    script_path = 'about.py'
    switch_to_script(script_path)

def switch_to_calc():
    script_path = 'calc.py'
    switch_to_script(script_path)

def switch_to_calendar():
    script_path = 'calendar.py'
    switch_to_script(script_path)

def switch_to_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error executing {script_path}")

while True:
    display_menu()

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        switch_to_filemgr()
    elif choice == 2:
        switch_to_cmd()
    elif choice == 3:
        switch_to_about()
    elif choice == 4:
        switch_to_calc()
    elif choice == 5:
        switch_to_calendar()
    elif choice == 6:
        print("Shutting Down..")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

import os
import subprocess
import platform

def display_prompt():
    print("\nTerminal")
    print("Available commands:")
    print("1. dir - List files in the current directory")
    print("2. echo <text> - Print the specified text")
    print("3. sysinfo - Display system information")
    print("4. open <script_name> - Open a script (calc, calendar, filemgr, about)")
    print("5. exit - Exit the program")

def list_files():
    files = os.listdir()
    print("\nFiles in the current directory:")
    for file in files:
        print(file)

def echo(text):
    print(f"\n{text}")

def display_sysinfo():
    system_info = platform.uname()
    print("\nSystem Information:")
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")
    print("SwagOS Version: 1.1")
    print("Python Version: 3.12.2")

def open_script(script_name):
    scripts = {
        'calc': 'calc.py',
        'calendar': 'calendar.py',
        'filemgr': 'filemgr.py',
        'about': 'about.py'
    }
    if script_name in scripts:
        subprocess.run(['python', scripts[script_name]])
    else:
        print(f"Script '{script_name}' not found.")

if __name__ == "__main__":
    while True:
        display_prompt()

        user_input = input("Enter a command: ").split(maxsplit=1)
        command = user_input[0].lower()

        if command == 'dir':
            list_files()
        elif command == 'echo':
            if len(user_input) > 1:
                text = user_input[1]
                echo(text)
            else:
                print("Invalid usage. Example: echo <text>")
        elif command == 'sysinfo':
            display_sysinfo()
        elif command == 'open':
            if len(user_input) > 1:
                script_name = user_input[1].lower()
                open_script(script_name)
            else:
                print("Invalid usage. Example: open <script_name>")
        elif command == 'exit':
            print("Exiting..")
            break
        else:
            print("Invalid command. Type 'exit' to exit the program.")

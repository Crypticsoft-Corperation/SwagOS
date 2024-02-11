import os
import subprocess
import platform

def display_prompt():
    print("\nTerminal")
    print("Available commands:")
    print("1. dir - List files in the current directory")
    print("2. cd <directory_path> - Change directory")
    print("3. echo <text> - Print the specified text")
    print("4. sysinfo - Display system information")
    print("5. exit - Exit the program")

def list_files():
    files = os.listdir()
    print("\nFiles in the current directory:")
    for file in files:
        print(file)

def change_directory(directory_path):
    try:
        os.chdir(directory_path)
        print(f"\nCurrent directory changed to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
    except PermissionError:
        print(f"Permission denied. Unable to change to {directory_path}")

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

if __name__ == "__main__":
    while True:
        display_prompt()

        user_input = input("Enter a command: ").split(maxsplit=1)
        command = user_input[0].lower()

        if command == 'dir':
            list_files()
        elif command == 'cd':
            if len(user_input) > 1:
                directory_path = user_input[1]
                change_directory(directory_path)
            else:
                print("Invalid usage. Example: cd <directory_path>")
        elif command == 'echo':
            if len(user_input) > 1:
                text = user_input[1]
                echo(text)
            else:
                print("Invalid usage. Example: echo <text>")
        elif command == 'sysinfo':
            display_sysinfo()
        elif command == 'exit':
            print("Exiting..")
            break
        else:
            print("Invalid command. Type 'exit' to exit the program.")

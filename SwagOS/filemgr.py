import os
import subprocess

def display_menu():
    print("Simple File Manager App")
    print("1. List files in the current directory")
    print("2. Create a new file")
    print("3. View file content")
    print("4. Delete a file")
    print("5. Exit")

def list_files():
    files = os.listdir()
    print("\nFiles in the current directory:")
    for file in files:
        print(file)

def create_file():
    filename = input("Enter the name of the new file: ")
    try:
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")
    except IOError as e:
        print(f"Error creating file: {e}")

def view_file():
    file_path = input("Enter the full path of the file to view: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"\nContent of '{file_path}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied. Unable to view '{file_path}'.")
    except Exception as e:
        print(f"Error reading file: {e}")

def delete_file():
    filename = input("Enter the name of the file to delete: ")
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied. Unable to delete '{filename}'.")

if __name__ == "__main__":
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            list_files()
        elif choice == 2:
            create_file()
        elif choice == 3:
            view_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            print("Exiting..")
            script_path = 'main.py'
            subprocess.run(['python', script_path])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

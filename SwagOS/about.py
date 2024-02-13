import subprocess

def about_program():
    print("About SwagOS")
    print("Crypticsoft SwagOS")
    print("Version 1.1")
    print("Python 3.12.2")
    print("Copyright 2022-2024 Crypticsoft Corperation. All rights reserved.")

    script_path = 'main.py'
    subprocess.run(['python', script_path])

if __name__ == "__main__":
    about_program()

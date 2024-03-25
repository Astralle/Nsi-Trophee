import os


def save_file():
    file_path = 'save.py'
    try:
        os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

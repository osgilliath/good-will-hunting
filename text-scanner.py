
import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    """Opens a file dialog to select a file and returns its path."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def print_file_extension(file_path):
    """Prints the extension of the given file."""
    if file_path:
        _, file_extension = os.path.splitext(file_path)
        if file_extension:
            print(f"File extension: {file_extension}")
        else:
            print("File has no extension.")

if __name__ == "__main__":
    selected_file = select_file()
    if selected_file:
        print(f"Selected file: {selected_file}")
        print_file_extension(selected_file)
    else:
        print("No file selected.")

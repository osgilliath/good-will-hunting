
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image
import pytesseract
from pypdf import PdfReader

def select_file():
   # This should open a dialog box, for you to select a file and will return the file path, hopefully.
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def print_file_extension(file_path):
    # This should return the extension of the selected file.
    if file_path:
        _, file_extension = os.path.splitext(file_path)
        return file_extension

def print_file_content(file_path):
    if file_path:
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']: # all image formats supported by PIL
            # If the selected file is an image
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(Image.open(file_path))
            print(text)
        elif file_extension.lower() == '.pdf':
            # If the selected file is a pdf
            reader = PdfReader(file_path)
            for page in reader.pages:
                text = page.extract_text()
                print(text)
        else:
            print("Unsupported file type.")

if __name__ == "__main__":
    selected_file = select_file() # Checks if a file is selected
    if selected_file:
        print(f"Selected file: {selected_file}") # Prints the selected file path
        print_file_content(selected_file) # Prints the content of the selected file
    else:
        print("No file selected.")

# Lot of work this took man, phewww...

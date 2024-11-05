import tkinter as tk
from tkinter import filedialog
'''
This is the main file that will be executed to generate the txt file with numbers from 1 to 300.
'''
def generate_txt_file():
    numbers = [str(i) for i in range(1, 301)]
    content = '\n'.join(numbers)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)
        print("File created successfully!")
def main():
    root = tk.Tk()
    root.withdraw()
    generate_txt_file()
if __name__ == "__main__":
    main()
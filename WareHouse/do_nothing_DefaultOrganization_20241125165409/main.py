'''
This is the main file of the software.
'''
import tkinter as tk
from utils import Utility
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Do Nothing Software")
        self.geometry("400x300")
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Click the button to do nothing.")
        self.label.pack(pady=20)
        self.button = tk.Button(self, text="Do Nothing", command=self.do_nothing)
        self.button.pack()
    def do_nothing(self):
        # Implement the do_nothing functionality here
        utility = Utility()
        utility.utility_function()
        utility.new_utility_function()
if __name__ == "__main__":
    app = Application()
    app.mainloop()
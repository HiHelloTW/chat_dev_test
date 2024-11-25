'''
This is the main file of the cat feeding application.
'''
import tkinter as tk
from cat_feeder import CatFeeder
class CatFeedingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cat Feeding App")
        self.cat_feeder = CatFeeder()
        self.create_widgets()
    def create_widgets(self):
        self.feed_button = tk.Button(self.master, text="Feed Cat", command=self.feed_cat)
        self.feed_button.pack()
    def feed_cat(self):
        self.cat_feeder.feed()
        print("Cat has been fed!")
root = tk.Tk()
app = CatFeedingApp(root)
root.mainloop()
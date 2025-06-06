import tkinter as tk
from tkinter import filedialog
import json

class Menu:
    def __init__(self,window, json_object):
        self.window = window
        self.json_object = json_object

        self.display_menu()

    def display_menu(self):
        
        menu_bar = tk.Menu(self.window)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", 
                              command = lambda: save_json_file(self.json_object) )
           #command = save_json_file(self.json_object) )
        file_menu.add_command(label="Open", command=do_something)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
       
        menu_bar.add_cascade(label="File",menu=file_menu)

        return menu_bar

def save_json_file(json_object):

    file_path = filedialog.asksaveasfilename(
            defaultextension=".json", 
            filetypes=[("JSON Files", "*.json")])

    if file_path:
        with open(file_path, 'w') as f:
            json.dump(json_object, f, indent=4)
        
def do_something():
    print("Menu item selected")


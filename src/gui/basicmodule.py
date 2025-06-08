import tkinter as tk
from tkinter import filedialog
import json

class Menu:
    def __init__(self,window, json_object, mW):
        self.window = window
        self.json_object = json_object

        self.display_menu()
        self.mW= mW
        self.mW.name= 'john'

    def display_menu(self):
        
        menu_bar = tk.Menu(self.window)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", 
                              command= lambda: new_warehouse_window(self.window))
        file_menu.add_command(label="Save", 
                              command = lambda: save_json_file(self.json_object) )
        file_menu.add_command(label="Open", 
                              command = lambda: open_json_file(self.json_object) )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
       
        menu_bar.add_cascade(label="File",menu=file_menu)
        mW.name='Claude'

        return menu_bar

def save_json_file(json_object):

    file_path = filedialog.asksaveasfilename(
            defaultextension=".json", 
            filetypes=[("JSON Files", "*.json")])

    if file_path:
        with open(file_path, 'w') as f:
            json.dump(json_object, f, indent=4)

def open_json_file(json_object):

    file_path = filedialog.askopenfilename(
            defaultextension=".json", 
            filetypes=[("JSON Files", "*.json")])

    if file_path:
        with open(file_path, 'r') as file:
            json_object = json.load(file)
    print(json_object)
    # Load from string
    json_string = '{"name": "John", "age": 30}'
    json_object = json.loads(json_string)
    print(json_object)


        
def do_something():
    print("Menu item selected")

def add_name_of_warehouse():
    print("The name of the warehouse")
    myWarehouse.name='Maryann'

def new_warehouse_window(root):

    new_window = tk.Toplevel(root)
    new_window.title("New Warehouse")
    new_window.geometry('400x300')
    
    menu_bar = tk.Menu(new_window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=new_window.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    new_window.config(menu=menu_bar)

    # Add widgets to the new window
    labelWarehouseName = tk.Label(new_window, text="Put in warehouse name")
    labelWarehouseName.pack(padx=20, pady=20)

    WarehouseName = tk.Text(new_window, height=1, width=30)
    WarehouseName.pack()

    button = tk.Button(new_window, text="Click Me", 
            command= add_name_of_warehouse )
    button.pack()



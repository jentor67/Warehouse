import tkinter as tk
from tkinter import filedialog
import json

class Menu:
    def __init__(self, window, json_object, mW):
        self.window = window
        self.json_object = json_object
        self.WarehouseNameTextBox = ''
        self.WarehouseDescriptionTextBox = ''
        self.display_menu()
        self.mW= mW

    class WarehouseAttributes:
        def __init__(self):
            self.Name = '' 
            self.Description = '' 


    def display_menu(self):
        
        menu_bar = tk.Menu(self.window)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", 
                command= self.new_warehouse_window )
        file_menu.add_command(label="Do", 
                command= self.do_something )
        file_menu.add_command(label="Save", 
                command = lambda: self.save_json_file(self.json_object) )
        file_menu.add_command(label="Open", 
                command = lambda: self.open_json_file(self.json_object) )

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=self.window.quit)
       
        menu_bar.add_cascade(label="File",menu=file_menu)

        return menu_bar


    def save_json_file(self,json_object):
    
        file_path = filedialog.asksaveasfilename(
                defaultextension=".json", 
                filetypes=[("JSON Files", "*.json")])
    
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(json_object, f, indent=4)
   

    def open_json_file(self,json_object):
    
        file_path = filedialog.askopenfilename(
                defaultextension=".json", 
                filetypes=[("JSON Files", "*.json")])
    
        if file_path:
            with open(file_path, 'r') as file:
                json_object = json.load(file)
        # Load from string
        json_string = '{"name": "John", "age": 30}'
        json_object = json.loads(json_string)
    
            
    def do_something(self):
        print("New warehouse name")
        print(self.mW.name, self.mW.description)
   

    def add_name_of_warehouse(self, window):
        # Warehouse name
        self.mW.name = self.WarehouseNameTextBox.get("1.0", "end-1c") 
        # Warehouse Description
        self.mW.description = self.WarehouseDescriptionTextBox.get("1.0", "end-1c") 
        window.destroy()


    def new_warehouse_window(self):
        warehouseAttributes = self.WarehouseAttributes

        new_window = tk.Toplevel(self.window)
        new_window.title("New Warehouse")
        new_window.geometry('400x300')
        
        menu_bar = tk.Menu(new_window)
    
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=new_window.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
    
        new_window.config(menu=menu_bar)
    
        # Add widgets to the new window
        labelWarehouseName = tk.Label(new_window, text="Warehouse name")
        labelWarehouseName.pack(padx=20, pady=20)
   
        # create text box of warehouse name
        self.WarehouseNameTextBox = tk.Text(new_window, height=1, width=30)
        self.WarehouseNameTextBox.pack()
   
        labelWarehouseDescription = tk.Label(
                new_window, 
                text="Warehouse Description")
        labelWarehouseDescription.pack(padx=20, pady=20)
   
        # create text box of warehouse name
        self.WarehouseDescriptionTextBox = tk.Text(
                new_window, 
                height=1, 
                width=30)
        self.WarehouseDescriptionTextBox.pack()
   
        # create button to update name
        button = tk.Button(new_window, text="Click Me", 
                command = lambda:self.add_name_of_warehouse( new_window) )
        button.pack()



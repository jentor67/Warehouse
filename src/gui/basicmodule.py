import tkinter as tk
from tkinter import filedialog
import json

class Menu:
    def __init__(self,window, json_object, mW):
        self.window = window
        self.json_object = json_object
        self.WarehouseName = ''
        self.WarehouseDescription = ''
        self.display_menu()
        self.mW= mW
        self.mW.name= 'john'

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
        #self.mW.name='Claude'

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
        print(json_object)
        # Load from string
        json_string = '{"name": "John", "age": 30}'
        json_object = json.loads(json_string)
        print(json_object)
    
            
    def do_something(self):
        print("New warehouse name")
        print(self.mW.name, self.mW.description)
   

    def add_name_of_warehouse(self, window):
        self.mW.name = self.WarehouseName.get("1.0", "end-1c") #Warehouse Name
        self.mW.description = self.WarehouseDescription.get("1.0", "end-1c") #Warehouse Name
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
        labelWarehouseName = tk.Label(new_window, text="Put in warehouse name")
        labelWarehouseName.pack(padx=20, pady=20)
   
        # create text box of warehouse name
        self.WarehouseName = tk.Text(new_window, height=1, width=30)
        self.WarehouseName.pack()
   
        # create text box of warehouse name
        self.WarehouseDescription = tk.Text(new_window, height=1, width=30)
        self.WarehouseDescription.pack()
   
        # create button to update name
        button = tk.Button(new_window, text="Click Me", 
                command = lambda:self.add_name_of_warehouse( new_window) )
        button.pack()



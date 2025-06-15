#!/usr/bin/python3
import tkinter as tk
import windowclass

class Menu(tk.Menu):
    def __init__(self, parent, theWarehouse):
        super().__init__(parent)

        self.WH = theWarehouse

        file_menu = tk.Menu(self, tearoff=False)

        self.add_cascade( label="File", underline=0, menu=file_menu)
        
        file_menu.add_command(label="New",
                command= lambda: windowclass.NewWarehouse(parent, theWarehouse) )
        
        file_menu.add_command(label="Do",
                command= self.do_something() )

        '''
        file_menu.add_command(label="Save",
                command = lambda: self.save_json_file(self.json_object) )
        file_menu.add_command(label="Open",
                command = lambda: self.open_json_file(self.json_object) )
        '''
        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=parent.quit)


    def do_something():
        print(self.WH.name)



class NewWareHouse(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade( label="File", underline=0, menu=file_menu)


        file_menu.add_separator()

        file_menu.add_command(label="Close", command=parent.destroy)


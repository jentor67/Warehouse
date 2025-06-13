#!/usr/bin/python3
# img_viewer.py
import basicmodule
import warehousemodule
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import json


def testButton():
    print(myWarehouse.name)


myWarehouse = warehousemodule.Warehouse

with open('/home/jmajor/Git/Warehouse/config/g_rack.json','r') as file:
    g_rack = json.load(file)


rack = json.loads('{ }')

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Warehouse Creator -- " + myWarehouse.name)

# Set geometry (widthxheight)
root.geometry('700x400')

# create Menu class
mainmenu = basicmodule.Menu(root,rack,myWarehouse)

# add menu to window
root.config( menu = mainmenu.display_menu())


button = tk.Button(root, text="Click Me",
        command = testButton )
button.pack()

root.mainloop()

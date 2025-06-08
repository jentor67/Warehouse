#!/usr/bin/python3
# img_viewer.py
import basicmodule
import warehousemodule
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import json


myWarehouse = warehousemodule.Warehouse

with open('/home/jmajor/Git/Warehouse/config/g_rack.json','r') as file:
    g_rack = json.load(file)


rack = json.loads('{ }')

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Warehouse Creator")

# Set geometry (widthxheight)
root.geometry('700x400')

myWarehouse.name = 'Anne-marie'
print(myWarehouse.name)
# create Menu class
mainmenu = basicmodule.Menu(root,rack,myWarehouse)

print(myWarehouse.name)
# add menu to window
root.config( menu = mainmenu.display_menu())

root.mainloop()

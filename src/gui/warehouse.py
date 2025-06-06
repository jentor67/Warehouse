#!/usr/bin/python3
# img_viewer.py
import basicmodule 
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import json



with open('/home/jmajor/Git/Warehouse/config/g_rack.json','r') as file:
    g_rack = json.load(file)

rack = json.loads('{ }')

# create root window
root = Tk()


# root window title and dimension
root.title("Welcome to Warehouse Creator")

# Set geometry (widthxheight)
root.geometry('700x400')


# create Menu class
#mainmenu = basicmodule.Menu(root,rack)


#root.config( menu = mainmenu.display_menu())
root.config( menu = basicmodule.Menu(root,rack) )

root.mainloop()

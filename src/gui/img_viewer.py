#!/usr/bin/python3
# img_viewer.py

from tkinter import *
import tkinter as tk

def do_something():
    print("Menu item selected")


def new_warehouse_window():


    new_window = tk.Toplevel(root)
    new_window.title("New Warehouse")
    new_window.geometry('400x300')
    
    menu_bar = tk.Menu(new_window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=new_warehouse_window)
    file_menu.add_command(label="Open", command=do_something)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    new_window.config(menu=menu_bar)

    # Add widgets to the new window
    label = tk.Label(new_window, text="This is a new window.")
    label.pack(padx=20, pady=20)
        

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Warehouse Creator")

# Set geometry (widthxheight)
root.geometry('700x400')

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_warehouse_window)
file_menu.add_command(label="Open", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()

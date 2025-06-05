#!/usr/bin/python3
# img_viewer.py

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import json

def do_something():
    print("Menu item selected")


def save_json_file():
    data_to_save = {}  # Dictionary to hold your data
    
    # Example: Get data from Tkinter widgets
    data_to_save["entry_value"] = entry.get()
    data_to_save["text_value"] = text_area.get("1.0", "end-1c") # Get full text content
    
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, 'w') as f:
            json.dump(g_rack, f, indent=4) # The indent makes it more readable
            #json.dump(data_to_save, f, indent=4) # The indent makes it more readable


def save_file():
    file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Data file", "*.json"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                text_to_save = text_area.get("1.0", tk.END)
                file.write(text_to_save)
        except Exception as e:
            print(f"Error saving file: {e}")

   

with open('/home/jmajor/Git/Warehouse/config/g_rack.json','r') as file:
    g_rack = json.load(file)



# create root window
root = Tk()

entry = tk.Entry(root)
entry.pack()

text_area = tk.Text(root)
text_area.pack()

# root window title and dimension
root.title("Welcome to Warehouse Creator")

# Set geometry (widthxheight)
root.geometry('700x400')

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
#file_menu.add_command(label="New", command=save_file)
file_menu.add_command(label="New", command=save_json_file)
file_menu.add_command(label="Open", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()

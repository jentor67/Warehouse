import tkinter as tk
from tkinter import filedialog
import json


def save_json_file(theClass):
   
    json_object = create_json_object(theClass)

    file_path = filedialog.asksaveasfilename(
            defaultextension=".json", 
            filetypes=[("JSON Files", "*.json")])
    
    if file_path:
        with open(file_path, 'w') as f:
            json.dump(json_object, f, indent=4)
   

def open_json_file(theClass):
    
    file_path = filedialog.askopenfilename(
            defaultextension=".json", 
            filetypes=[("JSON Files", "*.json")])
    
    if file_path:
        with open(file_path, 'r') as file:
            json_object = json.load(file)
    # Load from string
    #json_string = '{"name": "John", "age": 30}'
    #json_object = json.loads(json_string)
   
    theClass = load_json_object(theClass,json_object)


def load_json_object(theClass,json_ob):
    # create class
    theClass.name = json_ob['name']
    theClass.description = json_ob['description']
    
    return theClass
            

def create_json_object(theClass):
    # take the warehouse class and make it into a json object


    json_string = '{' +\
      '"name": "' + theClass.name + '", ' + \
      '"description": "' + theClass.description + '"}'
    

    json_object = json.loads(json_string)

    return json_object

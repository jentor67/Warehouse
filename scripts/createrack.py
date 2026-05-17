#23456789112345678921234567893123456789412345678951234567896123456789712
import bpy
import os
import json
import sys
from pathlib import Path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#sys.path.append('/path/to/your/script/folder')
# import functions.py
import functions as fun
import importlib
importlib.reload(fun) # reload
# Command line
#  blender --background --python createrack.py
# -------------------------------------------------


# ---------------------------------------------------
# Clean default scene
# ---------------------------------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


directory = os.path.dirname(os.path.abspath(__file__))
print("Hello")
print(directory)


#with open(directory + '../config/e03_rack.json','r') as file:
with open('../config/e01_rack.json','r') as file:
    rack = json.load(file)

fun.place_racks_json(rack)


# Output OBJ path
#output_path = directory + '../objects/E01.obj'

# Deselect everything
bpy.ops.object.select_all(action='DESELECT')

# Select all mesh objects
mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

for obj in mesh_objects:
    obj.select_set(True)

# Set active object (required for join)
bpy.context.view_layer.objects.active = mesh_objects[0]

# Join all selected meshes into one object
bpy.ops.object.join()

# Export the joined object
bpy.ops.wm.obj_export(
    filepath=directory + 'E01.obj',
    export_selected_objects=True
)

print("OBJ exported:", output_path)








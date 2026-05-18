#23456789112345678921234567893123456789412345678951234567896123456789712
import bpy
import os
import json
import sys
from pathlib import Path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# import functions.py
import functions as fun
import importlib
importlib.reload(fun) # reload


# Command line
#  blender --background --python createrack.py -- <configFile>
# -------------------------------------------------


# ---------------------------------------------------
# Clean default scene
# ---------------------------------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


# -----------------------------------------------
# read in argument
# ----------------------------------------------
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # everything after --
configFile = argv[0]
configFileName = Path(argv[0]).stem


directory = os.path.dirname(os.path.abspath(__file__))
configDirectory = str(Path(directory).parent) + '/config'
objectDirectory = str(Path(directory).parent) + '/object'
outputDirectory = Path('/mnt/kdrive/warehouse/objects')

jsonFile = configDirectory + '/' + configFile 

with open(jsonFile,'r') as file:
    rack = json.load(file)

fun.place_racks_json(rack)

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
outputFile = configFileName + '.obj'
output_path = outputDirectory / outputFile
bpy.ops.wm.obj_export(
    filepath= str(output_path),
    export_selected_objects=True
)

print("OBJ exported:", output_path)


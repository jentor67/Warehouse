#!/usr/bin/python3
import os
from pathlib import Path
import subprocess

directory = os.path.dirname(os.path.abspath(__file__))

configDirectory = str(Path(directory).parent) + '/config'


files = [f for f in os.listdir(configDirectory) if os.path.isfile(os.path.join(configDirectory, f))]


for f in files:
    # create the racks
    subprocess.run("blender --background --python createrack.py -- " + f, shell=True)


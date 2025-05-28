#!/usr/bin/python3
from jsonschema import validate
import simplejson as json
import json


with open('config/g_rack.json','r') as file:
    y = json.load(file)

print(y['name'])

print(y['bays'][2]['levels'][2])




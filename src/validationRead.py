#!/usr/bin/python3
from jsonschema import validate
import simplejson as json
import pandas as pd
import json


# A sample schema, like what we'd get from json.load()
with open('schema.json') as f:
    schema = json.load(f)

# If no exception is raised by validate(), the instance is valid.
with open('data.json') as g:
    data = json.load(g)

validate(instance=data, schema=schema)

#df = pd.read_json('test1.json')

#print(df)

with open('test1.json','r') as file:
    y = json.load(file)

print(y['name'])

print(y['bays'][2]['levels'][2])




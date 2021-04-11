#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import sys
import re

#URL     = "http://127.0.0.1:5000/bundler/fvtt/scenes"
URL     = "https://boisdechet.org/moulinette/bundler/fvtt/scenes"

if len(sys.argv) == 1:
  print("Usage: %s <folder>" % sys.argv[0])
  exit(1)

folder = sys.argv[1]

##
## Converts name into valid file name
##
def toFilename( name ):
  return re.sub('[^0-9a-zA-Z]+', '-', name.lower())

response = json.loads(requests.get(URL).text)
for el in response:
  #scene = el["scene"]
  
  id = toFilename(el["sceneName"])
  manifest = {
    "id": id,
    "name": el["sceneName"],
    "description": el["sceneDesc"],
    "type": "scenes",
    "source": el["authorImg"],
    "list": [
        {
            "name": "Inn.jpg",
            "url": el["imageURL"],
            "data": "/main/scenes/%s/%s1.json" % (folder, id)
        }
    ]
  }
  
  data = json.loads(el["scene"])
  data['name'] = el["sceneName"]
  data['tokens'] = []
  data['notes'] = []
  data['sounds'] = []
  data['navName'] = ""
  del data['img']
  
  with open('scenes/%s/%s.json' % (folder, id), 'w') as f:
    json.dump(manifest, f, indent=4) 

  with open('scenes/%s/%s1.json' % (folder, id), 'w') as f:
    json.dump(data, f, indent=4) 

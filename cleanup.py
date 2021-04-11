#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import json

PATH = os.path.dirname(__file__)

##
## Scenes
##
for root, dirs, files in os.walk(PATH + "/scenes"):
  for file in sorted(files): 
    if file.endswith('.json'): 
      path = os.path.join(root, file)
      scene = None
      with open(path) as f:
        scene = json.loads(f.read())
        # cleanup metadata files
        if not "type" in scene:
          if "img" in scene:
            print("Deleting img from %s" % path)
            del scene["img"]
          if "thumb" in scene:
            print("Deleting thumb from %s" % path)
            del scene["thumb"]
          if "_priorThumbPath" in scene:
            print("Deleting _priorThumbPath from %s" % path)
            del scene["_priorThumbPath"]
          if "tiles" in scene and len(scene["tiles"]) > 0:
            print("Deleting tiles from %s" % path)
            scene["tiles"] = []
          if "tokens" in scene and len(scene["tokens"]) > 0:
            print("Deleting tokens from %s" % path)
            scene["tokens"] = []
          if "notes" in scene and len(scene["notes"]) > 0:
            print("Deleting notes from %s" % path)
            scene["notes"] = []
        
        with open(path, "w") as f:
          json.dump(scene, f, indent=4)

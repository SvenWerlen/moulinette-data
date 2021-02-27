#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import json

PATH = os.path.dirname(__file__) + "/tokens"

packs = ""
frames = ""

SOURCES = { 
  "round-grey.png": "[VTTAssets](https://github.com/VTTAssets/vtta-tokenizer/tree/master/img)",
  "round-brown.png": "[VTTAssets](https://github.com/VTTAssets/vtta-tokenizer/tree/master/img)",
  "card-european.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2_1/Cards)",  
}

MARKDOWN = """
# Moulinette Tokens

Data packs and frames for [Moulinette Tokenizer](https://github.com/SvenWerlen/moulinette/tree/master/tokenizer/README.md)

## Data Packs

| :exclamation: *Previews below contain portions of images from the internet. These images are protected by the copyright of their owners.* |
| :----------------------------------------- |

| Name | Preview | Type | # tokens |
| --- | --- | --- | ---: |
{{PACKS}}

## Frames

| Name | Preview | Type | Source / copyrights |
| --- | --- | --- | --- |
{{FRAMES}}
"""

##
## Templates
##
for root, dirs, files in os.walk(PATH + "/packs"):
  for file in sorted(files): 
    if file.endswith('.json'): 
      path = os.path.join(root, file)
      with open(path) as f:
        data = json.loads(f.read())
        # ./tokens/packs/samples/dwarfs.json => Dwarfs
        name = os.path.split(path)[1].split(".")[0].replace("-", " ").title()
        # ./tokens/packs/samples/dwarfs.json => Round
        frame = data["frame"].title()
        # ./tokens/packs/samples/dwarfs.json => packs/samples/dwarfs.json
        url = path.split("/tokens/")[1]
        # ./tokens/packs/samples/dwarfs.json => packs/samples/dwarfs.png
        urlPreview = path.split("/tokens/")[1].replace(".json", ".png")
        
        packs += "| [%s](%s) | <img src=\"%s\" width=\"400\"> | %s | %d |\n" % (name, url, urlPreview, frame, len(data["list"]))
        

MARKDOWN = MARKDOWN.replace("{{PACKS}}", packs)

##
## Frames
##
for root, dirs, files in os.walk(PATH + "/frames"):
  for file in sorted(files): 
    if file.endswith('.png'): 
      path = os.path.join(root, file)
      # ./tokens/frames/card-european.png => European
      name = os.path.split(path)[1].split("-")[1].split(".")[0].title()
      # ./tokens/frames/card-european.png => Card
      frame = os.path.split(path)[1].split("-")[0].split(".")[0].title()
      # ./tokens/frames/card-european.png => frames/card-european.png
      url = path.split("/tokens/")[1]
      
      frames += "| [%s](%s) | <img src=\"%s\" width=\"64\"> | %s | %s |\n" % (name, url, url, frame, SOURCES[url.split("frames/")[1]])
        
MARKDOWN = MARKDOWN.replace("{{FRAMES}}", frames)

with open(PATH + "/README.md", "w") as f:
  f.write(MARKDOWN)
  f.close()

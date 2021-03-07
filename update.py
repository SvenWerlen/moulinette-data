#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import json

PATH = os.path.dirname(__file__)

packs = ""
frames = ""
playlists = ""
images = ""
scenes = ""

SOURCES = { 
  "round-grey.png": "[VTTAssets](https://github.com/VTTAssets/vtta-tokenizer/tree/master/img)",
  "round-brown.png": "[VTTAssets](https://github.com/VTTAssets/vtta-tokenizer/tree/master/img)",
  "card-european.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2_1/Cards)",
  "card-proxy.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2_1/Cards)",  
  "round-beige.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Smooth)",  
  "round-circuitboard.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Smooth)",  
  "round-cobblestone.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Smooth)",  
  "round-gear.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Gears)",  
  "round-greenproto.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Smooth)",  
  "round-lava.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Smooth)",
  "round-leaves.png": "[RPTools](https://github.com/RPTools/TokenTool/tree/main/src/main/resources/net/rptools/tokentool/overlays/v2/Round/Decorated)",  
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

MARKDOWN_BUNDLE = """
# Moulinette Bundler for FoundryVTT

Resources for [Moulinette Bundler for FoundryVTT](https://github.com/SvenWerlen/moulinette/tree/master/bundler/README.md)

{{INFOS}}

## List

| Name | Source / copyrights | # {{TYPE}} | Description / Preview |
| --- | --- | ---: | --- |
{{LIST}}

## Contribute

Are you interested in creating new bundles ? Check [how to contribute](CONTRIBUTE.md).

"""


##
## Templates
##
for root, dirs, files in os.walk(PATH + "/tokens/packs"):
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
for root, dirs, files in os.walk(PATH + "/tokens/frames"):
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

with open(PATH + "/tokens/README.md", "w") as f:
  f.write(MARKDOWN)
  f.close()


##
## Playlists
##
for root, dirs, files in os.walk(PATH + "/playlists"):
  for file in sorted(files): 
    if file.endswith('.json'): 
      path = os.path.join(root, file)
      with open(path) as f:
        data = json.loads(f.read())
        name = data["name"]
        # ./playlists/lists/spellcasting-chants-from-baldursgate1.json => lists/spellcasting-chants-from-baldursgate1.json
        url = path.split("/playlists/")[1]
        # "NeverWinterVault|https://neverwintervault.org/project/nwn2/audio/sound/spellcasting-chants-baldurs-gate-motb-version"
        source = data["source"].split('|')[0]
        sourceURL = data["source"].split('|')[1]
        
        playlists += "| [%s](%s) | [%s](%s) | %d | %s |\n" % (name, url, source, sourceURL, len(data["list"]), data['description'])
        

MARKDOWN_BUNDLE_PL = MARKDOWN_BUNDLE.replace("{{LIST}}", playlists).replace("{{TYPE}}", "sounds").replace("{{INFOS}}", "Playlists available as a new compendium. Don't forget to enable the module to see it in Foundry!")

with open(PATH + "/playlists/README.md", "w") as f:
  f.write(MARKDOWN_BUNDLE_PL)
  f.close()
  

##
## Images
##
for root, dirs, files in os.walk(PATH + "/images"):
  for file in sorted(files): 
    if file.endswith('.json'): 
      path = os.path.join(root, file)
      with open(path) as f:
        data = json.loads(f.read())
        name = data["name"]
        # ./images/lists/baldurs-portraits.json => lists/baldurs-portraits.json
        url = path.split("/images/")[1]
        # "Baldur's Gate Wiki|https://baldursgate.fandom.com/wiki/Portraits",   
        source = data["source"].split('|')[0]
        sourceURL = data["source"].split('|')[1]
        
        images += "| [%s](%s) | [%s](%s) | %d | %s |\n" % (name, url, source, sourceURL, len(data["list"]), data['description'])
        
MARKDOWN_BUNDLE_IMG = MARKDOWN_BUNDLE.replace("{{LIST}}", images).replace("{{TYPE}}", "images").replace("{{INFOS}}", "Browse `/module/<moulinette-name>/images/` in Foundry to find your images.")

with open(PATH + "/images/README.md", "w") as f:
  f.write(MARKDOWN_BUNDLE_IMG)
  f.close()


##
## Scenes
##
for root, dirs, files in os.walk(PATH + "/scenes"):
  for file in sorted(files): 
    if file.endswith('.json'): 
      path = os.path.join(root, file)
      with open(path) as f:
        data = json.loads(f.read())
        
        # ignore metadata files
        if not "type" in data or data["type"] != "scenes":
          continue
        
        if path.find("wfrp4e") > 0:
          continue;
        
        name = data["name"]
        # ./scenes/pathfinder/curse-crimson-throne-old-fishery.json => pathfinder/curse-crimson-throne-old-fishery.json
        url = path.split("/scenes/")[1]
        # "rpgmapshare.com/|http://rpgmapshare.com"
        source = data["source"].split('|')[0]
        sourceURL = data["source"].split('|')[1]
        
        thumb = "<img src=\"https://boisdechet.org/moulinette/static/thumbs/%s.webp\" width=\"200\" title=\"%s\"/>" % (data["id"], data["description"])
        print(thumb)
        
        scenes += "| [%s](%s) | [%s](%s) | %d | %s |\n" % (name, url, source, sourceURL, len(data["list"]), thumb)
        
MARKDOWN_BUNDLE_SCE = MARKDOWN_BUNDLE.replace("{{LIST}}", scenes).replace("{{TYPE}}", "scenes").replace("{{INFOS}}", "Scenes available as a new compendium. Don't forget to enable the module to see it in Foundry!")

with open(PATH + "/scenes/README.md", "w") as f:
  f.write(MARKDOWN_BUNDLE_SCE)
  f.close()

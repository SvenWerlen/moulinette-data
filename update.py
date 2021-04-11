#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import json

PATH = os.path.dirname(__file__)

scenes = ""
transl = ""

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
        
        thumb = "<img src=\"https://boisdechet.org/moulinette/static/thumbs/%s.webp\" width=\"200\" title=\"%s\"/>" % (data["id"], data["description"].replace("\"", "\\\""))
        
        scenes += "| [%s](%s) | [%s](%s) | %d | %s |\n" % (name, url, source, sourceURL, len(data["list"]), thumb)
        
MARKDOWN_BUNDLE_SCE = MARKDOWN_BUNDLE.replace("{{LIST}}", scenes).replace("{{TYPE}}", "scenes").replace("{{INFOS}}", "Scenes available as a new compendium. Don't forget to enable the module to see it in Foundry!")

with open(PATH + "/scenes/README.md", "w") as f:
  f.write(MARKDOWN_BUNDLE_SCE)
  f.close()


##
## Translations
##
for root, dirs, files in os.walk(PATH + "/translations"):
  for file in sorted(files): 
    if file.endswith('.json'): 
      path = os.path.join(root, file)
      with open(path) as f:
        data = json.loads(f.read())
        name = data["name"]
        # ./translations/babele/pf2-fr_vovf.json => babele/pf2-fr_vovf.json
        url = path.split("/translations/")[1]
        # pathfinder-fr|https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/tree/master/babele-alt/vo-vf/fr
        source = data["source"].split('|')[0]
        sourceURL = data["source"].split('|')[1]
        
        transl += "| [%s](%s) | [%s](%s) | %d | %s |\n" % (name, url, source, sourceURL, len(data["list"]), data['description'].replace("\"", "\\\""))
        
MARKDOWN_BUNDLE_TSL = MARKDOWN_BUNDLE.replace("{{LIST}}", transl).replace("{{TYPE}}", "transl").replace("{{INFOS}}", "Use Moulinette for Foundry VTT to manage your translations.")

with open(PATH + "/translations/README.md", "w") as f:
  f.write(MARKDOWN_BUNDLE_TSL)
  f.close()

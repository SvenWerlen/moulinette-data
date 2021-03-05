# Moulinette Bundler for FoundryVTT - Images

This page describes **How to contribute** by submiting new image packs.

## Prerequisites

* The images must be publiquely available on Internet

## Steps to create a bundle of images (novice)

* Prepare all the images by copying the URL to them into a text file 
* Submit the list of URLs by either
  * [Creating an issue on GitHub](https://github.com/SvenWerlen/moulinette-data/issues)
  * [Posting a message on Discord](https://discord.gg/xg3dcMQfP2)

## Steps to create a bundle of images (advanced contributor)

* Create the bundle manifest

```json
{
  "id": "<pack-id>",
  "name": "<pack-name>",
  "description": "<pack-description>",
  "type": "images",
  "source":  "<source-name>|<source-url>",
  "list": [
    {
      "name": "<image-name-1>",
      "url": "<url-to-image-1>"
    },
    {
      "name": "<image-name-2>",
      "url": "<url-to-image-2>"
    },
    ...
  ]
}
```

* **pack-id**: identifier of the pack. Must be unique. A folder with that name will be created in the module.
* **pack-name**: name of the pack. Displayed on [Moulinette Bundler](https://boisdechet.org/moulinette/bundler/fvtt/task) and [Readme](https://github.com/SvenWerlen/moulinette-data/tree/main/images).
* **pack-description**: description of the pack. Displayed on [Readme](https://github.com/SvenWerlen/moulinette-data/tree/main/images).
* **source-name** and **source-url**: source of the pack (where the image is from). Displayed on [Readme](https://github.com/SvenWerlen/moulinette-data/tree/main/images).
* **image-name-1**: name of the first image in the pack. Will be used as filename for the image.
* **url-to-image-1**: URL to the first image to download from Internet
* ...

*See [Baldur's gate portraits (example)](https://github.com/SvenWerlen/moulinette-data/blob/main/images/lists/baldurs1-portraits.json)*

Then:

* Create a pull request with the manifest file
* Submit and wait for approval

# Moulinette Bundler for FoundryVTT - Playlists

This page describes **How to contribute** by submiting new playlist packs.

## Prerequisites

* The sounds must be publiquely available on Internet

## Steps to create a bundle of playlists (novice)

* Prepare all the sounds by copying the URL to them into a text file 
* Submit the list of URLs by either
  * [Creating an issue on GitHub](https://github.com/SvenWerlen/moulinette-data/issues)
  * [Posting a message on Discord](https://discord.gg/xg3dcMQfP2)

## Steps to create a bundle of playlists (advanced contributor)

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
      "name": "<sound-name-1>",
      "url": "<url-to-sound-1>"
    },
    {
      "name": "<sound-name-2>",
      "url": "<url-to-sound-2>"
    },
    ...
  ]
}
```

* **pack-id**: identifier of the pack. Must be unique. A folder with that name will be created in the module.
* **pack-name**: name of the pack. Displayed on [Moulinette Bundler](https://boisdechet.org/moulinette/bundler/fvtt/task) and [Readme](https://github.com/SvenWerlen/moulinette-data/tree/main/playlists).
* **pack-description**: description of the pack. Displayed on [Readme](https://github.com/SvenWerlen/moulinette-data/tree/main/playlists).
* **source-name** and **source-url**: source of the pack (where the image is from). Displayed on [Readme](https://github.com/SvenWerlen/moulinette-data/tree/main/playlists).
* **sound-name-1**: name of the first sound in the pack. Will be used as display name in the playlist.
* **url-to-image-1**: URL to the first sound to download from Internet.
* ...

---

:information_source: you can use a url to a ZIP or RAR archive by using following notation `<url-to-archive>|<path-in-archive>`.

---

*See [Baldur's gate spellcasting chants (example)](https://github.com/SvenWerlen/moulinette-data/blob/main/playlists/lists/spellcasting-chants-from-baldursgate1.json)*

Then:

* Create a pull request with the manifest file
* Submit and wait for approval

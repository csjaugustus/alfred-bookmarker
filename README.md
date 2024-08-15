# Bookmarker

<p align="center">
  <img src="bookmarker-display-icon.png" alt="Bookmarker Logo" width="100" height="100">
</p>

An easier and more powerful way access and manage bookmarks in MacOS via Alfred, without being bound to any specific browser.

<p align="center">
  <img src="bookmarker-preview.gif" alt="Bookmarker Preview">
</p>

## Features

- **Two-Way Searching:** Bookmarks can be searched via their key or any of the URL links bound to them.
- **Fuzzy Matching**: Searching is made easy with fuzzy matching, which allows for partial matches and occasional typos.
- **Pinyin Support**: If the key of the bookmark is written fully or partially in Chinese, you will be able to match them using pinyin. Note however that fuzzy matching won't be applied in this case.
- **Bookmark Groups**: Instead of only binding a single URL to a bookmark, like how it is traditionally done in browsers, you can open any number of links using a single key.
- **Cross-browser Support**: Since your bookmarks are not stored to any browser in particular, you can always switch what browser to open bookmarks in.

## Installation

Install the following dependencies via pip: `pinyin`, `thefuzz`.

Download the workflow via [Releases](https://github.com/csjaugustus/alfred-bookmarker/releases).

Note that you will need to install them via the exact Python that Alfred uses; otherwise it leads to packages not being found. This notably causes issues when Python is installed via homebrew. Read [How to Install Python Dependencies](#how-to-install-python-dependencies) for more detailed info.

## Usage

- `b` - Search for bookmarks.
- `ab` - Add a bookmark. If the key doesn't already exist, it creates a new key and asks for URL(s); if it does, you will be adding URL(s) to a pre-existing entry.
- `db` - Delete a bookmark.
- `eb` - Edit bookmarks. This just opens the json file where all bookmarks are stored, allowing for easier editing. Use this if `ab` or `db` is too cumbersome.

## How to Install Python Dependencies

To ensure that dependencies are installed for the same Python that is used for the scripts in this workflow, you can open the workflow's directory and open any of the `.py` files. Then input this line at the very beginning:

```python
import sys

print(sys.executable)
```

Then turn on the debugger console in your Alfred workflow window. It should print the path of the Python executable.

For example if the path you get is `/opt/homebrew/opt/python@3.12/bin/python3.12`, you will need to install your packages like so:

```python
 /opt/homebrew/opt/python@3.12/bin/python3.12 -m pip install package_name --break-system-packages
```

(`--break-system-packages` is only required if the path is a homebrew one. Not including this will throw an error message.)

It is recommended to bind this to a snippet or snippet trigger for easier installation in the future.


# Bookmarker

<p align="center">
  <img src="bookmarker-display-icon.png" alt="Bookmarker Logo" width="100" height="100">
</p>

An easier and more powerful way access and manage bookmarks in MacOS via Alfred, without being bound to any specific browser.

<p align="center">
  <img src="bookmarker-preview.gif" alt="Bookmarker Preview">
</p>

# Features

- **Two-Way Searching:** Bookmarks can be searched via their key or any of the URL links bound to them.
- **Fuzzy Matching**: Searching is made easy with fuzzy matching, which allows for partial matches and occasional typos.
- **Pinyin Support**: If the key of the bookmark is written fully or partially in Chinese, you will be able to match them using pinyin. Note however that fuzzy matching won't be applied in this case.
- **Bookmark Groups**: Instead of only binding a single URL to a bookmark, like how it is traditionally done in browsers, you can open any number of links using a single key.
- **Cross-browser Support**: Since your bookmarks are not stored to any browser in particular, you can always switch what browser to open bookmarks in.

# Setup

## Installation
1. Download Alfred [here](https://www.alfredapp.com). Requires PowerPack.
2. Download Python [here](https://www.python.org/downloads/).
3. Get the latest version of the workflow via [Releases](https://github.com/csjaugustus/alfred-bookmarker/releases).

## Configuration
1. Once you install the workflow, you will need to run a setup to install the required dependencies (`thefuzz` and `pinyin`). You simply need to type this command in Alfred:

```
`bookmarker_setup
```

# Usage

- `b` - Search for bookmarks.
- `ab` - Add a bookmark. If the key doesn't already exist, it creates a new key and asks for URL(s); if it does, you will be adding URL(s) to a pre-existing entry.
- `db` - Delete a bookmark.
- `eb` - Edit bookmarks. This just opens the json file where all bookmarks are stored, allowing for easier editing. Use this if `ab` or `db` is too cumbersome.


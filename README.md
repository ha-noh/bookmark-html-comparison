# bookmark-html-comparison
Python script that compares two browser bookmark files and finds the unique urls between them. I wrote this to reconcile bookmark differences between browsers, specifically after importing my bookmarks to one browser but continuing to use the other.

## Usage
1. Add two exported bookmark files (`.html` files) to the directory containing `bkmrkcmp.py`. Name the older file `original.html` and the newer `modified.html`
2. Run `bkmrkcmp.py`
3. There should be a `results.txt` file in the same directory upon the program's completion
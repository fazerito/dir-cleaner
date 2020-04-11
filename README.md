# dir-cleaner
Simple directory cleaner written in Python

# Running script
**Always remember to make a backup of your files.**    

Download the script file, open the console in script's location and run
```cmd
python clean.py path/to/dir/to/clean
```

Script creates `images`, `docs`, `archives` and `exe` directories and moves files with certain extensions from path specified in command line to created folders.

Folders and extensions:  
`images` - e.g. .jpg, .gif, .png, .tiff, .blend  
`docs` - e.g. .doc, .pdf, .xls  
`archives` - e.g. .zip, .tar, .7z  
`exe` - .exe only  

Feel free to leave a comment with improvements.

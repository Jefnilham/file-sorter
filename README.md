# file-sorter
Assigns file types to subfolders according to file extensions in a given folder

# how it works
- The user will be prompted to enter filepath to a folder of choice
- The script creates subfolders ('Audio', 'Compressed', 'Documents', 'Codes', 'Images', 'Software', 'Videos', 'Others')
- Then it iterates through the given folder (ignoring existing folders) and moves files accordingly by reading file extensions
- Can set the script to run automatically via task scheduling / cronjob after editing folder input to a designated chosen folder

# how i use it
I set the path to only on my downloads folder and convert the script to an executable that will run periodically.

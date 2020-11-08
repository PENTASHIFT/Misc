import re
import os

# Stupid simple torrent organizer for my niche purposes.
# Symlinks all videos into a flat destination folder with prettier names.
# About it. 

EXT = ['.mkv', '.ogv', '.mp4']
TARGET = ""
DESTINATION = ""

def normalize(filename):
    filename = re.sub("\d{3,4}p.*", "", filename.lower())
    filename = re.sub("(web|blueray|bdrip|dvd).*", "", filename)
    filename = filename.split('.')
    filename = [word for word in filename if "." + word not in EXT]
    filename = " ".join([word.capitalize() for word in filename]).rstrip()

    return filename

def path_traverse(path):
    files = os.listdir(path)
    for f in files:
        if os.path.isdir(path + f):
            path_traverse(path + f)
        elif os.path.splitext(path + f)[1] in EXT:
            os.symlink(path + f,
                        DESTINATION + normalize(f) + os.path.splitext(path + f)[1])

if __name__ == '__main__':
    path_traverse(TARGET)

# An automated back-up script I threw together in a night.

# TODO:: Try to not have script break when it tries to run a directory.
# TODO:: Make this mess somewhat coherent.
# TODO:: Follow some sort of style guideline.

import os
from shutil import copy
from threading import Thread


# Pushes files to BACKUPDIR in parallel.
def backup(lst, homeDir):
    backupDir = '/home/<usr>/<path>' # Make sure to set your user and path here.

    for files in lst:
        home = homeDir + files
        backup = backupDir + files

        copy(home, backup)
        print("Moved: {0} to: {1}".format(files, backup))


# Send parsed files list to BACKUP.
def Main():
    homeDir = '/home/<usr>' # Make sure to set your user here.

    try:
        homeDir += input('> ')
        lst = os.listdir(homeDir)
    except:
        print("Please enter a valid directory.")
        Main()

    if len(lst)>1:
        mid = len(lst)//2
        topLst, btmLst = lst[:mid], lst[mid:]
    
        t1 = Thread(target=backup, args=(topLst, homeDir,))
        t2 = Thread(target=backup, args=(btmLst, homeDir,))
        t1.start()
        t2.start()
    else:
        print("Empty directory.")
        Main()


if __name__ == '__main__':
    Main()

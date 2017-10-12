#!/usr/bin/python3

""" An automated, functional backup script for *nix based systems.
    Utilizing parallel functionality to refrain from wasted time.
    Meant to have a udev rule applied to automatically run when
    an external drive is plugged in. """

import os
from shutil import copy
from threading import Thread

def identify(item, cwd):
    """ Recieves a single item from the tuple from BACKUP and checks
        whether it's a directory, if not it backs it up. """`
    cwd = os.path.join(cwd, item)
    if os.path.isdir(cwd):
        print('Parsing: %s.' %item)
        parse_dir(cwd)
    else:
        print('Copying: %s' %item)
        copy(cwd, end)

def backup(lst, cwd):
    """ Recieves half the tuple from PARSE_DIR and the directory then 
        maps the tuple to the identify function. """
    list(map(lambda x: identify(x, cwd), lst))

def parse_dir(cwd):
    """ Recieves the directory and then parses the contents 
        into a two item tuple to then backup in parallel. """
    lst = os.listdir(cwd)
    if not len(lst) <= 1:
        y, z = divmod(len(lst), 2)
        lst = (lst[:y + z], lst[y + z:])
        t1 = Thread(target=backup, args=(lst[0], cwd,))
        t2 = Thread(target=backup, args=(lst[1], cwd,))
        t1.start()
        t2.start()
    else:
        backup(lst, cwd)

# Meta Code.
start = '<directory to backup>'
end = '<ending directory here>'
parse_dir(start)

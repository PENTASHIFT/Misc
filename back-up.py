#!/usr/bin/env python3

""" An automated, functional backup script for *nix based systems.
    Utilizing parallel functionality to refrain from wasted time. """

import os
import sys
from shutil import copy
from threading import Thread

def backup(x):
    pass

def parse_dir(x):
    """ Recieves the directory and then parses the contents 
        into a two item tuple to then backup in parallel. """
    y, z = divmod(len(x), 2)
    return (x[:y + z], x[y + z:])
    

# PSEUDO-CODE
x = os.listdir('/home/gary/Pictures/')    
print(os.path.isdir(parse_dir(x[0])[0]))

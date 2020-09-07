# -*- encoding: utf-8 -*-

from platform import system, release

class OSOptions:
    '''Defines the OS-Options'''
    def __init__(self):
        self.OSName    = system()  # Get the name of the OS: ['linux', 'darwin', 'windows']
        self.OSRelease = release() # Get the OS Release, eg. '5.4.0-45-generic'
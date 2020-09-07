# -*- encoding: utf-8 -*-

import warnings
import subprocess
from platform import system, release

from ..exceptions import *

class OSOptions:
    '''Defines the OS-Options'''
    def __init__(self, rbin : str):
        self.rbin      = rbin      # Default Path to Rscripts
        self.OSName    = system()  # Get the name of the OS: ['linux', 'darwin', 'windows']
        self.OSRelease = release() # Get the OS Release, eg. '5.4.0-45-generic'
        
    @property
    def RAvailable(self):
        '''Check if R is available'''
        proc = subprocess.run('R --version', shell = True)
        
        if proc.returncode == 127:
            if self.rbin == None:
                warnings.warn('/bin/sh: 1: R: not found', DefaultPathWarning)
            return False
        
        return True
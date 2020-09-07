# -*- encoding: utf-8 -*-

__author__    = 'Debmalya Pramanik'
__copyright__ = f"Copyright (c) 2020 {__author__}"

__status__    = "development"

# Let's Check for the Dependencies
# hardDependencies    = [] # remove/update from setup.py
# missingDependencies = []

# for dependency in hardDependencies:
# 	try:
# 		__import__(dependency)
# 	except ImportError:
# 		missingDependencies.append(dependency)

# if missingDependencies:
# 	raise ImportError('Required Dependencies {}'.format(missingDependencies))

### --- Main Code --- ###
import subprocess

def ExecuteR(script : str, rbin : str = None):
    '''Execute R Code'''
    option = OSOptions(rbin = rbin)

    if option.RAvailable:
        subprocess.call (["/usr/bin/Rscript", "--vanilla", script])
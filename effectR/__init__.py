# -*- encoding: utf-8 -*-

__author__    = 'Debmalya Pramanik'
__copyright__ = f"Copyright (c) 2020 {__author__}"

__status__    = "development"

### --- Main Code --- ###
import warnings
import subprocess
from .exceptions import *
from .api import OSOptions

def ExecuteR(script : str, rbin : str = None, encoding = 'utf-8'):
    '''Execute R Code'''
    option = OSOptions(rbin = rbin)

    if option.RAvailable:
        proc = subprocess.run(["/usr/bin/Rscript", "--vanilla", script], capture_output = True)
    else:
        if (rbin == None) and ('linux' in option.OSName):
            _get_directory = subprocess.run(['which', 'R'], capture_output = True)
            rbin = _get_directory.stdout.decode(encoding)
            print('RBIN:', rbin)
            warnings.warn(f'Using R from {rbin}', FoundR)

        try:
            proc = subprocess.run([rbin, "--vanilla", script], capture_output = True)
        except FileNotFoundError as err:
            warnings.warn(f'Is R registered in $PATH? {err}', DefaultPathWarning)
            _get_directory = subprocess.run(['which', 'R'], capture_output = True)
            rbin = _get_directory.stdout.decode(encoding)

            if rbin:
                warnings.warn(f'Located R at {rbin}', FoundR)
                proc = subprocess.run([rbin, "--vanilla", script], capture_output = True)

    _stdin  = ' '.join(proc.args)
    _stdout = proc.stdout.decode(encoding)
    _stderr = proc.stderr.decode(encoding)

    return _stdin, _stdout, _stderr
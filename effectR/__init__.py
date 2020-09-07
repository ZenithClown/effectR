# -*- encoding: utf-8 -*-

__author__    = 'Debmalya Pramanik'
__copyright__ = f"Copyright (c) 2020 {__author__}"

__status__    = "development"

### --- Main Code --- ###
import subprocess
from .api import OSOptions

def ExecuteR(script : str, rbin : str = None, encoding = 'utf-8'):
    '''Execute R Code'''
    option = OSOptions(rbin = rbin)

    if option.RAvailable:
        proc = subprocess.run(["/usr/bin/Rscript", "--vanilla", script], capture_output = True)
    else:
        proc = subprocess.run([rbin, "--vanilla", script], capture_output = True)

    _stdin  = ' '.join(proc.args)
    _stdout = proc.stdout.decode(encoding)
    _stderr = proc.stderr.decode(encoding)

    return _stdin, _stdout, _stderr
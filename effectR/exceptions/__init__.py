# -*- encoding: utf-8 -*-

import warnings

class DefaultPathWarning(Warning):
    """Warning is raised if R is not available in default path /usr/bin"""
    def __str__(self):
        return 'If R is not installed in default /usr/bin then provide path in rbin command'
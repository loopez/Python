#!/usr/bin/env python
# -*- coding: utf-8 -*-
class couleur:
        CSI="\x1B["
        reset=CSI+"m"
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
print couleur.BOLD + "HELLO" + couleur.reset
print couleur.WARNING + ("HELLO") + couleur.reset

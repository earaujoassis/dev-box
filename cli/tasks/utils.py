# -*- coding: utf-8 -*-
# Copyright 2015 (c) Ewerton Assis
#

import sys

VAGRANT_SSH_CMD_FMT = "vagrant ssh -c \"{0}\" -- -q"


class ConsoleColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_green(message):
    sys.stdout.write(ConsoleColors.GREEN + message + ConsoleColors.END + '\n')


def print_error(message):
    sys.stdout.write(ConsoleColors.FAIL + message + ConsoleColors.END + '\n')

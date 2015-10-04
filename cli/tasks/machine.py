# -*- coding: utf-8 -*-
# Copyright 2015 (c) Ewerton Assis
#

import os
import sys
import time

from utils import VAGRANT_SSH_CMD_FMT, print_green, print_error


def console():
    os.system(VAGRANT_SSH_CMD_FMT.format('zsh'))


def halt():
    os.system('vagrant halt')


def run(command):
    os.system(VAGRANT_SSH_CMD_FMT.format(command))


def setup():
    os.system('vagrant up')
    time.sleep(15)
    os.system('vagrant up')
    run('/vagrant/cli/provision.sh')


def start():
    os.system('vagrant up')

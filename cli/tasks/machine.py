# -*- coding: utf-8 -*-
# Copyright 2015 (c) Ewerton Assis
#

import os
import sys
import time

from utils import VAGRANT_SSH_CMD_FMT, print_green, print_error
from utils import hook_file_path, remove_hook_file


def console():
    run('/bin/bash')


def halt():
    remove_hook_file()
    os.system('vagrant halt')


def reload():
    remove_hook_file()
    os.system('vagrant reload')


def run(command):
    return os.system(VAGRANT_SSH_CMD_FMT.format(command))


def setup():
    print_green('# Setting up the Vagrant machine')
    os.system('vagrant up')
    time.sleep(15)
    os.system('vagrant up')
    print_green('# Start provision')
    run('/vagrant/cli/provision.sh')
    print_green('# Setup complete')


def start():
    os.system('vagrant up')


def stream(command):
    if not os.path.isfile(hook_file_path):
        print_error("Error: there's not any active hook")
        return
    return run('cd /hook && {0}'.format(command))

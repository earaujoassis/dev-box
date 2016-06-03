# -*- coding: utf-8 -*-
# Copyright 2015 (c) Ewerton Assis
#

import os
import sys
import time
import shutil

from utils import root, VAGRANT_SSH_CMD_FMT, print_green, print_error, mkdirp
from utils import hook_file_path, remove_hook_file


def console():
    run('/bin/zsh')


def cook(path, caller_cwd):

    def delete_if_exists(path):
        if os.path.isfile(path):
            os.remove(path)

    local_cwd = os.getcwd()
    # Check if `path` is an absolute path to the recipe
    if os.path.isabs(path):
        recipe_path = os.path.realpath(path)
        recipe_basename = os.path.basename(recipe_path)
        mkdirp('.recipes')
        delete_if_exists(os.path.join(local_cwd, '.recipes', recipe_basename))
        shutil.copyfile(recipe_path, os.path.join(local_cwd, '.recipes', recipe_basename))
        recipe_path = os.path.join('/vagrant', '.recipes', recipe_basename)
    # Check if `path` is a relative path to the recipe (from the caller's perspective)
    elif os.path.isfile(os.path.realpath(os.path.join(caller_cwd, path))):
        recipe_path = os.path.realpath(os.path.join(caller_cwd, path))
        recipe_basename = os.path.basename(recipe_path)
        mkdirp('.recipes')
        delete_if_exists(os.path.join(local_cwd, '.recipes', recipe_basename))
        shutil.copyfile(recipe_path, os.path.join(local_cwd, '.recipes', recipe_basename))
        recipe_path = os.path.join('/vagrant', '.recipes', recipe_basename)
    # Check if `path + (.sh)` is a relative path to the recipe (from the dev-box's perspective)
    elif os.path.isfile(os.path.realpath(os.path.join(local_cwd, 'recipes', path + '.sh'))):
        recipe_path = os.path.realpath(os.path.join(local_cwd, 'recipes', path + '.sh'))
        recipe_basename = os.path.basename(recipe_path)
        recipe_path = os.path.join('/vagrant', 'recipes', recipe_basename)
    # Recipe file was not found
    else:
        print_error('Error: recipe was not found')
        return
    print_green('# DevBox is now cooking')
    return run('sh {0}'.format(recipe_path))


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
    return run('cd /home/vagrant/hook && {0}'.format(command))

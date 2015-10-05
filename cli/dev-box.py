#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015 (c) Ewerton Assis
#

import argparse
import sys
import os

import tasks
from tasks import utils
from tasks.utils import root

parser = argparse.ArgumentParser(description='DevBox CLI tool and manager')
subparsers = parser.add_subparsers(dest='parent')
hook = subparsers.add_parser('hook', help='create a hook to a given directory')
hook.add_argument('dir', action='store')
subparsers.add_parser('unhook', help='release any active hook')
subparsers.add_parser('console', help='open a bash console inside the machine')
subparsers.add_parser('halt', help='halt the Vagrant machine')
subparsers.add_parser('reload', help='reload the Vagrant machine')
subparsers.add_parser('run', help='run a command inside the Vagrant machine') \
    .add_argument('commands', action='store', nargs=argparse.REMAINDER)
subparsers.add_parser('setup', help='setup the Vagrant machine')
subparsers.add_parser('start', help='start the Vagrant machine')


class DevBoxCLI(object):

    def __init__(self, namespace = None, original_cwd = ''):
        self.original_cwd = original_cwd
        self.namespace = namespace
        self

    def action(self):
        namespace = self.namespace
        parent = self.get_module_attribute_safely('parent', tasks)
        if parent is None:
            utils.print_error('Error: Command is not implemented yet')
            return
        subcommand = self.get_module_attribute_safely('subcommand', parent)
        if subcommand is None and not hasattr(parent, '__call__'):
            utils.print_error('Error: Task is not implemented yet')
            return
        elif type(subcommand) is list:
            if hasattr(parent, 'servant'):
                servant = getattr(parent, 'servant')
                return servant(subcommand)
            else:
                utils.print_error('Error: Cannot run subcommand sequence')
                return
        if subcommand is None:
            task_function = parent
        else:
            task_function = subcommand
        if hasattr(namespace, 'commands'):
            commands = getattr(namespace, 'commands')
            return task_function(' '.join(commands))
        if hasattr(namespace, 'argument'):
            return task_function(namespace.argument)
        if hasattr(namespace, 'dir'):
            return task_function(namespace.dir, self.original_cwd)
        return task_function()

    def get_module_attribute_safely(self, reference, module):
        namespace = self.namespace
        if hasattr(namespace, reference):
            attr = getattr(namespace, reference)
            if type(attr) is list:
                return attr
            attrname = attr.replace('-', '_')
            if hasattr(module, attrname):
                return getattr(module, attrname)
        return None

    @staticmethod
    def apply(argv):
        original_cwd = os.getcwd()
        os.chdir(root)
        namespace = parser.parse_args(argv[1:])
        return DevBoxCLI(namespace, original_cwd).action()


if __name__ == '__main__':
    code = DevBoxCLI.apply(sys.argv)
    sys.exit(code)

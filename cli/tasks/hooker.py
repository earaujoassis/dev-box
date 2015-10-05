# -*- coding: utf-8 -*-
# Copyright 2015 (c) Ewerton Assis
#

import os
import sys
import datetime
import json

from utils import root, hook_file_path, vm_id_file_path
from utils import print_error, print_green, remove_hook_file
from machine import run as vagrant_run


def hook(path, caller_cwd):
    if os.path.isfile(hook_file_path):
        print_error("Error: there's an active hook; unhook it first")
        return
    if os.path.isfile(vm_id_file_path):
        with open(vm_id_file_path) as vm_id_file:
            vm_id = vm_id_file.read()
    else:
        print_error('Error: VM ID was not found')
        return
    if os.path.isabs(path):
        hook_path = os.path.realpath(path)
    else:
        hook_path = os.path.realpath(os.path.join(caller_cwd, path))
    dev_box_path = os.path.realpath(root)
    if dev_box_path == hook_path:
        print_error('Error: Inceptions are not allowed here, sorry')
        return
    rc = 0
    rc += os.system("VBoxManage sharedfolder add {0} --name hook --hostpath {1} --transient".format(vm_id, hook_path))
    rc += os.system("VBoxManage setextradata {0} VBoxInternal2/SharedFoldersEnableSymlinksCreate/hook 1".format(vm_id))
    rc += vagrant_run('sudo mkdir -p /hook')
    rc += vagrant_run('sudo chown -R vagrant:vagrant /hook')
    rc += vagrant_run('sudo mount -t vboxsf -o uid=1000,gid=1000 hook /hook')
    if rc == 0:
        hook_hash = {}
        hook_hash['path'] = hook_path
        hook_hash['created_at'] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        hook_hash['vm_id'] = vm_id
        hook_hash['status'] = 'created'
        hook_json = json.dumps(hook_hash, sort_keys=False, indent=4, separators=(',', ': '))
        hook_file = open(hook_file_path, 'w+')
        hook_file.write(hook_json)
        hook_file.write('\n')
        print(hook_json)
    else:
        print_error('Error: something went bad! Hook was not properly created')


def unhook():
    if not os.path.isfile(hook_file_path):
        print_error("Error: there's not any active hook")
        return
    if os.path.isfile(hook_file_path):
        with open(hook_file_path) as hook_file:
            hook_hash = json.loads(hook_file.read())
            vm_id = hook_hash['vm_id']
    rc = 0
    rc += vagrant_run('sudo umount -a -t vboxsf /hook')
    rc += os.system("VBoxManage sharedfolder remove {0} --name hook --transient".format(vm_id))
    if rc == 0:
        remove_hook_file()
        hook_hash['status'] = 'destroyed'
        hook_json = json.dumps(hook_hash, sort_keys=False, indent=4, separators=(',', ': '))
        print(hook_json)
    else:
        print_error('Error: something went bad! Hook was not properly released. Is there any active hook?')

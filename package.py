# -*- coding: utf-8 -*-

name = 'tk_core'

version = "0.19.10"

description = 'tk-core'

authors = ['ShotgunSoftware']

tools = []

requires = [
    'python-2.7',
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env.PYTHONPATH.append("{root}/python")
    env.SG_CONFIG_FILE = '{root}/config/core/shotgun.yml'
    env.SGTK_CORE_LOCATION = '{root}'


format_version = 2

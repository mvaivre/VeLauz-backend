#!/bin/sh

virtualenv --no-site-packages env
env/bin/easy_install "pyramid==1.4.5"
env/bin/python setup.py develop

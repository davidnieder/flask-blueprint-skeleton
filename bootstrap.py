#!/usr/bin/env python2

import sys
import subprocess


PYTHON = 'python2'
PYPI_BASE_URL = 'https://pypi.python.org/packages/source/v/virtualenv/'
PYPI_PKG = 'virtualenv-12.0.7'
PKG_EXT = '.tar.gz'
VENV_DIR = 'venv/'
TMP_DIR = '_bootstrap/'
REQUIREMENTS_FILE = 'requirements.txt'

def execute(cmd):
    re = subprocess.call(cmd, stdout=sys.stdout, stderr=sys.stderr, shell=True)
    if re != 0:
        print '"%s" failed with exit code %i' %(cmd, re)
        sys.exit(1)

# create temporary directory
execute('mkdir %s' %TMP_DIR)
# download virtualenv
execute('curl -so %s%s%s %s%s%s' %(TMP_DIR,PYPI_PKG,PKG_EXT,PYPI_BASE_URL,
                                   PYPI_PKG,PKG_EXT))
# extract archive
execute('tar -xzf %s%s%s -C %s' %(TMP_DIR,PYPI_PKG,PKG_EXT,TMP_DIR))
# create virtual environment
execute('%s %s%s/virtualenv.py -q %s' %(PYTHON, TMP_DIR,PYPI_PKG,VENV_DIR))
# install requirements with pip
execute('%sbin/pip install -qr %s' %(VENV_DIR,REQUIREMENTS_FILE))
# cleaning up
execute('rm -r %s' %TMP_DIR)

print 'Done'
sys.exit(0)


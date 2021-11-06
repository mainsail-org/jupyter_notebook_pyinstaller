# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

from logging import getLogger

logger = getLogger(__name__)  # you can use other name

HERE = os.path.dirname(__file__)

# os.environ['JUPYTERLAB_SETTINGS_DIR'] = str(os.path.join(HERE, 'settings'))

import jupyterlab_server
from jupyterlab.labapp import LabApp
from jupyterlab_server import LabServerApp, LabConfig
from notebook.base.handlers import IPythonHandler, FileFindHandler
from notebook.utils import url_path_join as ujoin
import json
from traitlets import Unicode

import sys
from os.path import realpath
from os import getcwd
me = realpath(sys.argv[0])
logger.debug("Using %s as binary", me)
args = []
args.extend(["--notebook-dir=" + getcwd(),
	# If this is being run as a subcommand, be sure to insert it here, below example is for subcommand notebook
    # and also using argparse, note the -- to terminate argument parsing
    # "--KernelManager.kernel_cmd=['"+me+"', 'notebook', 'kernel', '--', '-f', '{connection_file}']"])
    "--KernelManager.kernel_cmd=['" + me + "', 'ipykernel_launcher', '-f', '{connection_file}']"])
logger.info("notebook argv: %s", str(args))

if __name__ == '__main__':
     LabApp.launch_instance(argv=args)


# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

HERE = os.path.dirname(__file__)

# os.environ['JUPYTERLAB_SETTINGS_DIR'] = str(os.path.join(HERE, 'settings'))

import jupyterlab_server
from jupyterlab.labapp import LabApp
from jupyterlab_server import LabServerApp, LabConfig
from notebook.base.handlers import IPythonHandler, FileFindHandler
from notebook.utils import url_path_join as ujoin
import json
from traitlets import Unicode


if __name__ == '__main__':
    LabApp.launch_instance()

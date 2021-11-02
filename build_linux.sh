#!/bin/bash
pyinstaller jupyter_notebook.spec --clean --strip --onefile --icon=app.ico
mkdir -p /Users/mireille/opensource/biometix-support/jupyter_notebook_pyinstaller/dist/jupyter_notebook/debugpy/_vendored

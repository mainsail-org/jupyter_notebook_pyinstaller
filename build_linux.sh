#!/bin/bash
pyinstaller jupyter_notebook.spec --clean --strip --onefile --noconfirm --icon=app.ico
mkdir -p /Users/mireille/opensource/biometix-support/jupyter_notebook_pyinstaller/dist/jupyter_notebook/debugpy/_vendored
cp package.json dist/jupyter_notebook/
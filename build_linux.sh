#!/bin/bash
rm -f -R dist/
rm -f -R build/
pyinstaller jupyter_notebook.spec --clean --strip --onefile --noconfirm --target-architecture="arm64" --collect-all="jupyterlab" --collect-all="jupyterlab_server"
mkdir -p dist/jupyter_notebook/debugpy/_vendored
cp package.json dist/jupyter_notebook/
# mkdir dist/jupyter_notebook/jupyter_server
# cp -R /Users/mireille/Desktop/test1/env1/lib/python3.8/site-packages/jupyter_server ./dist/jupyter_notebook/jupyter_server

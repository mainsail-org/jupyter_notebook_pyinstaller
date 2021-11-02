#!//usr/bin/env python3
from logging import getLogger

logger = getLogger(__name__)  # you can use other name


def jupyter_notebook():
    import sys
    from os.path import realpath
    from os import getcwd
    me = realpath(sys.argv[0])
    logger.debug("Using %s as binary", me)

    argm = [me, '-m' , 'ipykernel_launcher', '-f', '{connection_file}' ]
   
    arg_notebook = []
    arg_notebook.extend(["--notebook-dir=" + getcwd(),
                 # If this is being run as a subcommand, be sure to insert it here, below example is for subcommand notebook
                 # and also using argparse, note the -- to terminate argument parsing
                 # "--KernelManager.kernel_cmd=['"+me+"', 'notebook', 'kernel', '--', '-f', '{connection_file}']"])
                 "--KernelManager.kernel_cmd=['" + me + "'-m , 'ipykernel_launcher', '-f', '{connection_file}']"])

    logger.info(sys.path)
    from notebook import notebookapp
    notebookapp.launch_new_instance(argv=argm)
    # from ipykernel import kernelapp as app 
    # app.launch_new_instance()

if __name__ == "__main__":
    import sys
    from logging import basicConfig, DEBUG

    basicConfig(level=DEBUG)
    jupyter_notebook()

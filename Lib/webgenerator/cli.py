#! usr/bin/env python

import os
import sys
from webgenerator.webgenerator import logger, setLoglevel
from webgenerator.webgenerator import main as main_
def main():
    setLoglevel(logger, 'DEBUG')
    # the last if 2 args second to last if more than 2 arguments
    sourcepath = os.path.abspath(sys.argv[max(-2, 1 - len(sys.argv))]) \
                                    if len(sys.argv) >= 2 else os.getcwd()
    destination = None
    # If there are 3 (or more?) args, the last one sets a destination directory and
    # the website will be generated in there instead of running the development
    # server.
    if len(sys.argv) >= 3:
        destination = os.path.abspath(sys.argv[-1])

    logger.debug(f'sourcepath: {sourcepath}')
    logger.debug(f'destination: {destination}')

    main_(sourcepath, destination)

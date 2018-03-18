"""Common objects shared by all Glances modules."""

import errno
import os
import sys

# Operating system flag
# Note: Somes libs depends of OS
BSD = sys.platform.find('bsd') != -1
LINUX = sys.platform.startswith('linux')
MACOS = sys.platform.startswith('darwin')
SUNOS = sys.platform.startswith('sunos')
WINDOWS = sys.platform.startswith('win')

# Set the AMPs, plugins and export modules path
work_path = os.path.realpath(os.path.dirname(__file__))
amps_path = os.path.realpath(os.path.join(work_path, 'amps'))
plugins_path = os.path.realpath(os.path.join(work_path, 'plugins'))
exports_path = os.path.realpath(os.path.join(work_path, 'exports'))
sys_path = sys.path[:]
sys.path.insert(1, exports_path)
sys.path.insert(1, plugins_path)
sys.path.insert(1, amps_path)


def safe_makedirs(path):
    """A safe function for creating a directory tree."""
    try:
        os.makedirs(path)
    except OSError as err:
        if err.errno == errno.EEXIST:
            if not os.path.isdir(path):
                raise
        else:
            raise
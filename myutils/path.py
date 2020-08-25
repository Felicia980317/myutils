import os
import errno
from glob import glob


def make_sure_path_exists(path):
    """
    reference https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def walk(path):
    out = []
    for _path in glob(path):
        out += [_path.replace("\\", "/")]
    return out

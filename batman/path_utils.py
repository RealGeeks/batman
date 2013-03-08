import os


def normalize_path(path):
    """
    >>> normalize_path("~/ssh")
    '/home/kevin/ssh'
    >>> normalize_path("/home/kevin/ssh")
    '/home/kevin/ssh'
    """
    return os.path.abspath(os.path.expanduser(path))

import os


def normalize_path(path, basedir=None):
    """
    Just a utility function that will both expand user paths if they are there:
    >>> normalize_path("~/ssh")
    '/home/kevin/ssh'

    but won't if they are not
    >>> normalize_path("ssh")
    'ssh'

    and you can pass a basepath to combine
    >>> normalize_path("ssh","foo")
    '/foo/ssh'

    and wont' mess up absolute paths:
    >>> normalize_path("/home/kevin/ssh")
    '/home/kevin/ssh'
    """
    out = os.path.expanduser(path)
    if not os.path.isabs(path) and basedir:
        out = os.path.join(basedir, out)

    return out

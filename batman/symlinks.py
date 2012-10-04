import os
from utils import normalize_path


def ensure(links, basedir):
    for src, dst in links.iteritems():
        if not os.path.isabs(src):
            src = os.path.join(basedir, src)
        dst = normalize_path(dst)
        if not os.path.islink(dst):
            print "linking {src} to {dst}".format(src=src, dst=dst)
            os.symlink(src, dst)

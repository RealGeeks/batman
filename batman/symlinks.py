import os
from utils import normalize_path

def add_basepath(path, basedir):
    if not os.path.isabs(path):
        path = os.path.join(basedir, path)
    return  path

def ensure(links, basedir):
    for target, link_name in links.iteritems():
        target, link_name = add_basepath(normalize_path(target), basedir), add_basepath(normalize_path(link_name), basedir)

        if os.path.exists(link_name) and not os.path.islink(link_name):
            # Non-link file exists.  Delete but warn
            print "WARNING: Deleting non-link file {0}".format(link_name)
            os.remove(link_name)
        if os.path.islink(link_name) and os.readlink(link_name) != target:
            # Link exists but points to the wrong place
            os.unlink(link_name)
        if not os.path.islink(link_name):
            print "creating link at {link_name} pointing to {target}".format(link_name=link_name, target=target)
            os.symlink(target, link_name)

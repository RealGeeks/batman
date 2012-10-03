import os

def ensure(links):
    for src, dst in links.iteritems():
        if not os.lstat(src) and os.path.islink(src):
            os.symlink(src,dst)
            

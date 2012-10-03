import os
from hashtools import file_has_changed
from run import run

def check_and_update(stuff, hash_dir, basename, config_hash):
    for k, v in stuff.iteritems():
        print "CHECKING {0}".format(k)
        if file_has_changed(os.path.join(basename, k), hash_dir, config_hash):
            print "{0} HAS CHANGED!".format(k)
            run(v, virtualenv=True)
            
            

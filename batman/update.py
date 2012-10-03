import os
from hashtools import file_has_changed, update_hash
from run import run


def check_and_update(stuff, hash_dir, basedir, config_hash, virtualenv):
    for k, v in stuff.iteritems():
        print "CHECKING {0}".format(k)
        if file_has_changed(os.path.join(basedir, k), hash_dir, config_hash):
            print "{0} HAS CHANGED!".format(k)
            ret = run(v, virtualenv=virtualenv, in_dir=basedir)
            if ret.returncode == 0:
                # Command was successful
                update_hash(os.path.join(basedir, k), hash_dir, config_hash)
            else:
                # Command failed
                print "FAILURE RUNNING COMMAND {0}".format(v)
                print ret.stderr

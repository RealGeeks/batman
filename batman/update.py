import os
from batman.hashtools import file_has_changed, update_hash
from batman import dictchanged
from batman.run import run


def check_and_update(stuff, hash_dir, basedir, virtualenv):
    #Only update changed keys (filter stuff to only include changed keys)
    changed_keys = dictchanged.changed_keys(stuff, hash_dir)
    for k, v in stuff.iteritems():
        print "CHECKING {0}".format(k)
        need_to_run_command = file_has_changed(os.path.join(basedir, k), hash_dir or k in changed_keys)
        if need_to_run_command:
            print "{0} HAS CHANGED!".format(k)
            ret = run(v, virtualenv=virtualenv, in_dir=basedir, print_output=True)
            if ret.returncode == 0:
                # Command was successful
                update_hash(os.path.join(basedir, k), hash_dir)
            else:
                # Command failed
                print "FAILURE RUNNING COMMAND {0}".format(v)
                print ret.output

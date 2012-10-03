import os
import hashlib
import yaml


def hash_cfg_file(filename):
    with open(os.path.expanduser(filename)) as f:
        return hashlib.sha1(f.read()).hexdigest()


def load(filename):
    with open(os.path.expanduser(filename)) as f:
        out = yaml.load(f)
        out['hash'] = hash_cfg_file(filename)
        return out

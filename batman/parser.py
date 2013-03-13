import os
import hashlib
import yaml


def load(filename):
    with open(os.path.expanduser(filename)) as f:
        out = yaml.load(f)
        return out

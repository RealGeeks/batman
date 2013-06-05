import os
import yaml
from batman.yaml_ordered_dict import OrderedDictYAMLLoader


def load(filename):
    with open(os.path.expanduser(filename)) as f:
        out = yaml.load(f, Loader=OrderedDictYAMLLoader)
        return out

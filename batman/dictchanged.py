import os
import yaml
from batman.yaml_ordered_dict import OrderedDictYAMLLoader

OLD_DICT_FILENAME = 'old_dict.yml'

def _old_dict_filename(persist_dir):
    return os.path.join(os.path.expanduser(persist_dir), OLD_DICT_FILENAME)

def _make_dirs_if_not_exists(persist_dir):
    if not os.path.exists(persist_dir):
        os.makedirs(persist_dir)

def _write_old_dict(input, persist_dir):
    _make_dirs_if_not_exists(os.path.expanduser(persist_dir))
    with open(_old_dict_filename(persist_dir), 'w+') as f:
        f.write(yaml.dump(input))

def _load_old_dict(persist_dir):
    try:
        contents = open(_old_dict_filename(persist_dir)).read()
        return yaml.load(contents, Loader=OrderedDictYAMLLoader)
    except IOError:
        return {}

def _dict_compare(d1, d2):
    """
    We care if one of two things happens:

      * d2 has added a new key
      * a (value for the same key) in d2 has a different value than d1

    We don't care if this stuff happens:

      * A key is deleted from the dict

    Should return a list of keys that either have been added or have a different value than they used to

    """
    keys_added = set(d2.keys()) - set(d1.keys())
    keys_changed = [k for k in d1.keys() if k in d2.keys() and d1[k] != d2[k]]
    return list(keys_added) + keys_changed

def changed_keys(new_dict, persist_dir):
    old_dict = _load_old_dict(persist_dir)
    _write_old_dict(new_dict, persist_dir)
    if old_dict:
        return _dict_compare(old_dict, new_dict)
    else:
        return new_dict.keys()

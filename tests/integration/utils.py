import os
import tempfile
import shutil
import yaml
from contextlib import contextmanager

def touch_file(path):
    open(path, 'w')


@contextmanager
def batman_dir(definition):
    d = tempfile.mkdtemp()
    with open(os.path.join(d, '.batman.yml'), 'wc') as f:
        f.write(yaml.dump(definition))
    yield d
    shutil.rmtree(d)


def update_batman_yml(tmp_batman_dir, new_yml_dict):
        with open(os.path.join(tmp_batman_dir,'.batman.yml'),'a') as yml_file:
            yaml.dump(new_yml_dict, yml_file)

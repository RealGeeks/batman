import os
import tempfile
import shutil
import yaml
from contextlib import contextmanager

@contextmanager
def batman_dir(definition):
    d = tempfile.mkdtemp()
    with open(os.path.join(d, '.batman.yml'), 'wc') as f:
        f.write(yaml.dump(definition))
    yield d
    shutil.rmtree(d)

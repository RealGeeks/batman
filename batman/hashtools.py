import os
from run import run


def recursive_hash(dir):
    return run('tar -c {0} 2> /dev/null | sha1sum'.format(dir))[0]


class HashChecker(object):
    def __init__(self, file_to_check, hash_dir, cfg_hash):
        self.file_to_check = file_to_check
        hash_dir = os.path.expanduser(hash_dir)
        if not os.path.exists(hash_dir):
            os.makedirs(hash_dir)
        self.current_hash_file = os.path.join(hash_dir, file_to_check.replace('/', '_') + '.' + cfg_hash + '.md5')

    def get_current_hash(self):
        return recursive_hash(self.file_to_check)

    def get_stored_hash(self):
        try:
            with open(self.current_hash_file) as chf:
                return chf.read()
        except IOError:
            return False

    def update_hash(self):
        with open(self.current_hash_file, 'wc') as cf:
            cf.write(self.get_current_hash())

    def does_hash_match(self):
        return self.get_current_hash() == self.get_stored_hash()

    def has_changed(self):
        if not self.does_hash_match():
            return True
        return False


def file_has_changed(filename, hash_dir, cfg_hash):
    hc = HashChecker(filename, hash_dir, cfg_hash)
    return hc.has_changed()


def update_hash(filename, hash_dir, cfg_hash):
    hc = HashChecker(filename, hash_dir, cfg_hash)
    return hc.update_hash()

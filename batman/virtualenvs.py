from run import run
from utils import normalize_path


def check_virtualenv_exists(virtualenv_name, shell=True, pty=False, combine_stderr=False):
    return run('workon {0}'.format(virtualenv_name)).returncode == 0


def create_if_not_exists(virtualenv_name):
    if not check_virtualenv_exists(virtualenv_name):
        run('mkvirtualenv {0}'.format(virtualenv_name))


def sync_add2virtualenv(paths, virtualenv):
    run('rm "$(virtualenvwrapper_get_site_packages_dir)/_virtualenv_path_extensions.pth"', virtualenv=virtualenv)
    for path in paths:
        run('add2virtualenv {0}'.format(normalize_path(path)), virtualenv=virtualenv)

import os
import sys
import argparse
import virtualenvs
import parser
import update
import symlinks
import delete

BATMAN_FILE = '.batman.yml'


def parse_basedir():
    p = argparse.ArgumentParser(description='manage deployment')
    p.add_argument('project_directory', help='path to the project to process')
    args = p.parse_args()
    return os.path.abspath(args.project_directory)


def go(basedir, file=BATMAN_FILE):
    cfg = parser.load(os.path.join(basedir, file))
    if cfg.get('virtualenv'):
        virtualenvs.create_if_not_exists(cfg['virtualenv'])
    if cfg.get('add2virtualenv'):
        virtualenvs.sync_add2virtualenv(
            cfg['add2virtualenv'],
            cfg['virtualenv'],
        )
    if cfg.get('ensure_symlinks'):
        symlinks.ensure(cfg['ensure_symlinks'], basedir)
    if cfg.get('delete_pattern'):
        delete.delete_pattern(directory=basedir, pattern=cfg['delete_pattern'])
    if cfg.get('update_on_change'):
        update.check_and_update(
            cfg['update_on_change'],
            cfg['hash_dir'],
            basedir,
            cfg['hash'],
            cfg.get('virtualenv'),
        )


def main():
    basedir = parse_basedir()
    go(basedir)
    sys.exit(0)

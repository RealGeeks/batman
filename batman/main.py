import os
import virtualenvs
import parser
import update
import sys
import argparse

def main():
    p = argparse.ArgumentParser(description='manage deployment')
    p.add_argument('project_directory', help='path to the project to process')
    args = p.parse_args()
    basedir = args.project_directory
    file = basedir + '/.batman.yml'
    cfg = parser.load(file)
    virtualenvs.create_if_not_exists(cfg['virtualenv'])
    update.check_and_update(cfg['update_on_change'], cfg['hash_dir'], basedir, cfg['hash'])

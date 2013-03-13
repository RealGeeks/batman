import os
import fcntl
import select
import subprocess
from collections import namedtuple

Result = namedtuple('Result', 'output returncode')


def _prep_command(command, virtualenv, in_dir):
    prefix = 'WORKON_HOME=$HOME/.virtualenvs && source virtualenvwrapper.sh &&'
    if in_dir:
        prefix += "cd {0} && ".format(in_dir)
    if virtualenv:
        prefix += "workon {0} && ".format(virtualenv)
    return ['/usr/bin/env', 'bash', '-c'] + [prefix + command]


def _run_popen(command, print_output=False):
    """
    subprocess has the most terrible interface ever.
    Envoy is an option but too heavyweight for this.
    This is a convenience wrapper around subprocess.Popen.

    Also, this merges STDOUT and STDERR together, since
    there isn't a good way of interleaving them without
    threads.
    """
    output = ''
    po = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    fcntl.fcntl(
        po.stdout.fileno(),
        fcntl.F_SETFL,
        fcntl.fcntl(po.stdout.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK,
    )
    while po.poll() is None:
        stream = po.stdout
        readx = select.select([stream.fileno()], [], [])[0]
        if readx:
            chunk = stream.read()
            output += chunk
            if print_output:
                print chunk
    return Result(output, po.returncode)


def run(command, virtualenv=False, in_dir=False, print_output=False):
    command = _prep_command(command, virtualenv, in_dir)
    return _run_popen(command, print_output=print_output)


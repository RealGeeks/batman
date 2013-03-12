import os
import fcntl
import select
import subprocess
from utils import memoize
from collections import namedtuple

Result = namedtuple('Result', 'output returncode')

@memoize
def _bash_login_output():
    output, returncode =  _run_popen(['/usr/bin/env', 'bash', '-l', '-c', ''] ,print_output=False)
    return output

def _prep_command(command, virtualenv, in_dir):
    if in_dir:
        command = "cd {0} && ".format(in_dir) + command
    if virtualenv:
        command = "workon {0} && ".format(virtualenv) + command
    return ['/usr/bin/env', 'bash', '-l', '-c'] + [command]


def _run_popen(command, print_output=False):
    """
    subprocess has the most terrible interface ever.
    Envoy is an option but too heavyweight for this.
    This is a convenience wrapper around subprocess.Popen.
    """
    output = ''
    po = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    fcntl.fcntl(
        po.stdout.fileno(),
        fcntl.F_SETFL,
        fcntl.fcntl(po.stdout.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK,
    )
    while po.poll() is None:
        for stream in [po.stdout, po.stderr]:
            readx = select.select([stream.fileno()], [], [])[0]
            if readx:
                chunk = stream.read()
                output += chunk
                if print_output:
                    print chunk
    return output, po.returncode


def run(command, virtualenv=False, in_dir=False, print_output=False):
    command = _prep_command(command, virtualenv, in_dir)
    output, returncode = _run_popen(command, print_output=print_output)
    if output.endswith(_bash_login_output()):
        output = output[:-len(_bash_login_output())]
    return Result(output, returncode)


from collections import namedtuple
import subprocess

Result = namedtuple('Result', 'stderr stdout returncode')


def run(command, virtualenv=False, in_dir=False):
    """
    subprocess has the most terrible interface ever.
    Envoy is an option but too heavyweight for this.
    This is a convenience wrapper around subprocess.Popen.
    """
    if in_dir:
        command = "cd {0} && ".format(in_dir) + command
    if virtualenv:
        command = "workon {0} && ".format(virtualenv) + command
    runme = ['/bin/bash', '-c', '-l'] + [command]
    po = subprocess.Popen(runme, stdout=subprocess.PIPE)
    output = po.communicate()
    return Result(output[0], output[1], po.returncode)

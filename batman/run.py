from collections import namedtuple
import subprocess

Result = namedtuple('Result', 'output returncode')


def run(command, virtualenv=False, in_dir=False, stderr=subprocess.STDOUT):
    """
    subprocess has the most terrible interface ever.
    Envoy is an option but too heavyweight for this.
    This is a convenience wrapper around subprocess.Popen.
    """
    if in_dir:
        command = "cd {0} && ".format(in_dir) + command
    if virtualenv:
        command = "workon {0} && ".format(virtualenv) + command
    output = ''
    runme = ['/bin/bash', '-c', '-l'] + [command]
    po = subprocess.Popen(runme, stdout=subprocess.PIPE)
    while po.poll() is None:
        line = po.stdout.readline()
        if line:
            print line
            output += line
    return Result(output, po.returncode)

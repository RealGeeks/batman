from collections import namedtuple
import subprocess

Result = namedtuple('Result', 'stderr stdout returncode')

def run(command, virtualenv= False):
    if virtualenv:
        command = "workon {0} ".format(virtualenv) + command
    runme = ['/bin/bash','-c','-l'] + [command]
    po = subprocess.Popen(runme, stdout=subprocess.PIPE)
    output = po.communicate()
    return Result(output[0],output[1],po.returncode)

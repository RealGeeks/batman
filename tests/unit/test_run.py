import mock
from batman.run import run


@mock.patch('batman.run._run_popen')
def test_that_bash_is_prepended(mr):
    run('ls')
    assert mr.call_args[0][0] == ['/usr/bin/env', 'bash', '-l', '-c', 'ls']


@mock.patch('batman.run._run_popen')
def test_workon_is_prepended(mr):
    run('ls', virtualenv='foo')
    assert mr.call_args[0][0] == ['/usr/bin/env', 'bash', '-l', '-c', 'workon foo && ls']


@mock.patch('batman.run._run_popen')
def test_in_dir_calls_cd(mr):
    run('ls', in_dir='foo')
    assert mr.call_args[0][0] == ['/usr/bin/env', 'bash', '-l', '-c', 'cd foo && ls']

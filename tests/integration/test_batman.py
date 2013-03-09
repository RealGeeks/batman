import os
from batman.run import run
from tests.integration.utils import batman_dir, touch_file


# Virtualenv support

def test_that_virtualenv_is_created():
    with batman_dir({"virtualenv": "__batman__testenv"}) as tmp_batman_dir:
        os.system('batman {0}'.format(tmp_batman_dir))
        output = '__batman__testenv' in run('lsvirtualenv').output
    run("rmvirtualenv __batman__testenv")
    assert output

# Delete support

def test_that_files_are_deleted():
    with batman_dir({'delete_pattern': "*.poop"}) as tmp_batman_dir:
        touch_file(os.path.join(tmp_batman_dir, 'deleteme.poop'))
        os.system('batman {0}'.format(tmp_batman_dir))
        assert 'deleteme' not in run('ls {0}'.format(tmp_batman_dir)).output


def test_that_files_are_recursively_deleted():
    with batman_dir({'delete_pattern': "*.poop"}) as tmp_batman_dir:
        os.mkdir(os.path.join(tmp_batman_dir, 'something'))
        touch_file(os.path.join(tmp_batman_dir, 'something', 'deleteme.poop'))
        os.system('batman {0}'.format(tmp_batman_dir))
        assert 'deleteme' not in run('ls {0}'.format(tmp_batman_dir)).output

# Update support


def test_that_update_on_change_is_run_if_file_is_changed(tmpdir):
    with batman_dir({
        "hash_dir": str(tmpdir),
        "update_on_change": {
            "monkey.txt": "touch bananas.txt"
        }
    }) as tmp_batman_dir:
        touch_file(os.path.join(tmp_batman_dir, 'monkey.txt'))
        os.system('batman {0}'.format(tmp_batman_dir))
        touch_file(os.path.join(tmp_batman_dir, 'monkey.txt'))
        os.system('batman {0}'.format(tmp_batman_dir))
        assert 'bananas.txt' in run('ls {0}'.format(tmp_batman_dir)).output


def test_that_update_on_change_is_run_if_file_is_created(tmpdir):
    with batman_dir({
        "hash_dir": str(tmpdir),
        "update_on_change": {
            "monkey.txt": "touch bananas.txt"
        }
    }) as tmp_batman_dir:
        os.system('batman {0}'.format(tmp_batman_dir))
        touch_file(os.path.join(tmp_batman_dir, 'monkey.txt'))
        os.system('batman {0}'.format(tmp_batman_dir))
        assert 'bananas.txt' in run('ls {0}'.format(tmp_batman_dir)).output


def test_that_update_on_change_is_not_run_if_file_is_not_changed(tmpdir):
    with batman_dir({
        "hash_dir": str(tmpdir),
        "update_on_change": {
            "monkey.txt": "touch bananas.txt"
        }
    }) as tmp_batman_dir:
        os.system('batman {0}'.format(tmp_batman_dir))
        dirlisting = run('ls -la', in_dir=tmp_batman_dir).output
        os.system('batman {0}'.format(tmp_batman_dir))
        assert run('ls -la', in_dir=tmp_batman_dir).output == dirlisting

# Symlink support

def test_that_symlinks_are_created():
    with batman_dir({
        "ensure_symlinks": {
            "cotts.txt": "ravine.txt"
        }
    }) as tmp_batman_dir:
        os.system('batman {0}'.format(tmp_batman_dir))
        assert os.path.realpath(os.path.join(tmp_batman_dir, 'ravine.txt')) == os.path.join(tmp_batman_dir, 'cotts.txt')

# test_that_add2virtualenv_works

def test_that_virtualenv_is_created(tmpdir):
    TEST_PYTHON_FILENAME = '__batman_testfile.py'
    TEST_VIRTUALENV = '__batman_testenv'
    test_python_file = os.path.join(str(tmpdir), TEST_PYTHON_FILENAME)
    with batman_dir({
        "virtualenv": TEST_VIRTUALENV,
        "add2virtualenv": [str(tmpdir)],
    }) as tmp_batman_dir:
        touch_file(test_python_file)
        os.system('batman {0}'.format(tmp_batman_dir))
        output = TEST_PYTHON_FILENAME in run('lssitepackages', virtualenv=TEST_VIRTUALENV).output
    run("rmvirtualenv {0}".format(TEST_VIRTUALENV))

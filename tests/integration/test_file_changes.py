import os
from batman.run import run
from tests.integration.utils import batman_dir, update_batman_yml, touch_file

def test_that_batmanyml_changes_are_noticed():
    """
    Sometimes we need to change the .batman.yml file, so make sure that changes are noticed
    and get run.
    """
    with batman_dir({
        "ensure_symlinks": {
            "cotts.txt": "ravine.txt"
        }
    }) as tmp_batman_dir:
        os.system('batman {0}'.format(tmp_batman_dir))
        assert os.path.realpath(os.path.join(tmp_batman_dir, 'ravine.txt')) == os.path.join(tmp_batman_dir, 'cotts.txt')
        with open(os.path.join(tmp_batman_dir,'.batman.yml'),'a') as yml_file:
            update_batman_yml(tmp_batman_dir, {'ensure_symlinks': { 'cotts2.txt':'ravine2.txt'}})
        os.system('batman {0}'.format(tmp_batman_dir))
        assert os.path.realpath(os.path.join(tmp_batman_dir, 'ravine2.txt')) == os.path.join(tmp_batman_dir, 'cotts2.txt')

def test_that_on_update_commands_dont_get_rerun(tmpdir):
    """
    Should keep track of yaml stuff on a key-by-key basis and only rerun commands if
    that specific piece has changed.
    """
    test_yml = {
        "hash_dir": str(tmpdir),
        "update_on_change": {
            "monkey.txt": "echo '.' >> onedot.txt"
        }
    }
    with batman_dir(test_yml) as tmp_batman_dir:
        touch_file(os.path.join(tmp_batman_dir, 'monkey.txt'))
        os.system('batman {0}'.format(tmp_batman_dir))
        test_yml['update_on_change']['walrus.txt'] = 'touch bucket.txt'
        update_batman_yml(tmp_batman_dir, test_yml)
        os.system('batman {0}'.format(tmp_batman_dir))
        assert run('cat onedot.txt', in_dir=tmp_batman_dir).output == '.\n'

def test_that_on_update_commands_still_get_rerun_if_file_is_updated(tmpdir):
    test_yml = {
        "hash_dir": str(tmpdir),
        "update_on_change": {
            "monkey.txt": "echo '.' >> onedot.txt"
        }
    }
    with batman_dir(test_yml) as tmp_batman_dir:
        touch_file(os.path.join(tmp_batman_dir, 'monkey.txt'))
        os.system('batman {0}'.format(tmp_batman_dir))
        run('echo "updated" > monkey.txt', in_dir=tmp_batman_dir)
        os.system('batman {0}'.format(tmp_batman_dir))
        assert run('cat onedot.txt', in_dir=tmp_batman_dir).output == '.\n.\n'

def test_wildcard_expansion(tmpdir):
    with batman_dir({
        "hash_dir": str(tmpdir),
        "update_on_change": {
            "*/migrations/*": "echo '.' >> onedot.txt"
        }
    }) as tmp_batman_dir:
        testpath = os.path.join(tmp_batman_dir, 'testapp', 'migrations')
        os.makedirs(testpath)
        os.system('batman {0}'.format(tmp_batman_dir))
        touch_file(os.path.join(testpath, 'imhere.txt'))
        os.system('batman {0}'.format(tmp_batman_dir))
        run('echo "bleh" > {0}'.format(os.path.join(tmp_batman_dir, 'imhere.txt')))
        assert run('cat onedot.txt', in_dir=tmp_batman_dir).output == '.\n.\n'

def test_create_old_dict_if_not_exists(tmpdir):
    """
    If the hashdir doesnt exist, create it.
    """
    test_hashdir = os.path.join(str(tmpdir), 'hashdir/')

    with batman_dir({
        "hash_dir": test_hashdir,
        "update_on_change": {
            "monkey.txt": "echo '.' >> onedot.txt"
        }
    }) as tmp_batman_dir:
        os.system('batman {0}'.format(tmp_batman_dir))
        assert(os.path.isfile(os.path.join(test_hashdir, 'old_dict.txt')))


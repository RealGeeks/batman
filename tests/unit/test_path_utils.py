import os
from batman.path_utils import normalize_path

def test_that_normlalize_path_expands_tilde():
    home_path = os.path.expanduser("~")

    assert normalize_path("~/foo") == os.path.join(home_path, "foo")

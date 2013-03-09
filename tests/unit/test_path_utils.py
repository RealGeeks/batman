import os
from batman.path_utils import normalize_path

def test_that_normlalize_path_expands_tilde():
    home_path = os.path.expanduser("~")

    assert normalize_path("~/foo") == os.path.join(home_path, "foo")

def test_that_normalize_path_doesnt_expand_to_home_directory():
    assert normalize_path("test.txt") == "test.txt"

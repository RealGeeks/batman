import mock
from batman.dictchanged import _dict_compare, changed_keys

def test_keys_added():
    d1 = {}
    d2 = {'a':1}
    assert _dict_compare(d1, d2) == ['a']

def test_keys_removed():
    d1 = {'a':1}
    d2 = {}
    assert _dict_compare(d1, d2) == []

def test_key_value_changed():
    d1 = {'a':1}
    d2 = {'a':2}
    assert _dict_compare(d1, d2) == ['a']

def test_nothing_changed():
    d1 = {'a':1}
    d2 = {'a':1}
    assert _dict_compare(d1, d2) == []

@mock.patch('batman.dictchanged._write_old_dict')
@mock.patch('batman.dictchanged._load_old_dict')
def test_that_write_and_load_are_called(_load_old_dict, _write_old_dict):
    _load_old_dict.return_value = {'a':1}
    changed_keys({'a':1}, 'foo')
    _load_old_dict.assert_called()
    _write_old_dict.assert_called_with({'a':1}, 'foo')


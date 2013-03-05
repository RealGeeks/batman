import mock
from batman.delete import delete_pattern


@mock.patch('batman.run')
def test_delete_pattern(mr):
    delete_pattern('foo', 'bar')
    assert mr.called_with('cd foo && find . -name "bar" -print -delete')

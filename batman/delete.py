from run import run


def delete_pattern(pattern):
    """
    Finds and deletes all files matching `pattern`

    Be careful with this, for obvious reasons.
    """

    run('find . -name "{0}" -print -delete'.format(pattern))

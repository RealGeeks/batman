from run import run


def delete_pattern(directory, pattern):
    """
    Finds and deletes all files matching `pattern`

    Be careful with this, for obvious reasons.
    """

    run('cd {0} && find . -name "{1}" -print -delete'.format(
        directory,
        pattern
        ))

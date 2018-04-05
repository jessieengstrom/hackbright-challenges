"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    return rev(astring, [])


def rev(string, reverse):
    if len(string) == 0:
        return string
    elif len(string) == 1:
        reverse.append(string[0])
    else:
        reverse.append(string[-1])
        rev(string[:-1], reverse)

    return ''.join(reverse)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"

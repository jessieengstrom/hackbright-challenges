"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    largest = 0
    mode = set()
    for count in counts:
        if counts[count] > largest:
            if len(mode) > 0:
                mode = set([count])
            else:
                mode.add(count)
            largest = counts[count]
        elif counts[count] == largest:
            mode.add(count)

    return mode

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"

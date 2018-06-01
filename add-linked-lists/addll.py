"""Given two linked lists, treat them like numbers and add them together.

This should take two linked lists in "reverse-digit" format, sum them up,
and return the head of a new linked list in "reverse-digit" format.

A list is in reverse-digit format if it is each digit as a node, in
least-significant-place-first order. For example, "123", would become
the list 3->2->1.

Let's add 1 + 2::

    >>> l1 = Node(1)
    >>> l2 = Node(2)
    >>> add_linked_lists(l1, l2).as_rev_string()
    '3'

Let's add 123 + 456::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '579'

Let's make sure we carry: 144 + 456:

    >>> l1 = Node(4, Node(4, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '600'

Let's make sure it works with mismatched lengths: 123 + 89::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(9, Node(8))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '212'

"""

class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """
    # head = tail = None
    # carry = 0

    # while l1 or l2:

    #     if l1:
    #         digit1 = l1.data
    #         l1 = l1.next
    #     else:
    #         digit1 = 0

    #     if l2:
    #         digit2 = l2.data
    #         l2 = l2.next
    #     else:
    #         digit2 = 0

    #     digit = digit1 + digit2 + carry
    #     carry, digit = divmod(digit, 10)

    #     if not head:
    #         head = tail = Node(digit)

    #     else:
    #         tail.next = Node(digit)
    #         tail = tail.next

    # if carry:
    #     tail.next = Node(carry)

    # return head

    return all(l1, l2, 0)

def all(l1, l2, carry):

    if l1 is None and l2 is None and carry == 0:
        return None

    data = carry

    if l1 != None:
        data += l1.data

    if l2 != None:
        data += l2.data

    new_node = Node(data % 10)

    if l1 != None or l2 != None:

        l1_next = None if l1 is None else l1.next
        l2_next = None if l2 is None else l2.next
        carry = 1 if data >= 10 else 0
        next_n = all(l1_next, l2_next, carry)

        new_node.next = next_n

    return new_node


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"

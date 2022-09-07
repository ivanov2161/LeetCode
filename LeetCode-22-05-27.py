def romanToInt(s):
    """
    Difficult - Easy
    Convert Roman numerals to arabic numerals
    :param s:
    :return: Arabic number
    """

    # Constraints

    assert 1 <= len(s) <= 15

    # Solution
    answer = 0
    temp = s

    dictionary = (('CM', 900), ('M', 1000), ('CD', 400), ('D', 500), ('XC', 90), ('C', 100),
                  ('XL', 40), ('L', 50), ('IX', 9), ('X', 10), ('IV', 4), ('V',  5), ('I', 1))

    for key, value in dictionary:
        if temp.count(key):
            answer += temp.count(key) * value
            temp = temp.replace(key, '')
    return answer


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Difficult - Medium
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a
        linked list.
        EXAMPLE: Input: l1 = [2,4,3], l2 = [5,6,4]
                Output: [7,0,8]
                Explanation: 342 + 465 = 807.
        :type l1: ListNode
        :type l2: ListNode
        :return: ListNode
        """

        # Solution

        temp_int = 0

        def print_nodes(node):
            while node:
                print(node.val, end=' ' if node.next else '\n')
                node = node.next

        def reverse_list(head, tail=None):
            while head:
                head.next, tail, head = tail, head, head.next
            return tail

        def node_to_int(node):
            number = ''
            while node:
                number += str(node.val)
                node = node.next
            return int(number)

        def append(node, val):
            end = ListNode(val)
            n = node
            while (n.next):
                n = n.next
            n.next = end

        def int_to_listnode(node, number):
            for i in str(number):
                append(node, int(i))
            return node

        temp_int = node_to_int(reverse_list(l1)) + node_to_int(reverse_list(l2))
        temp_node = ListNode()
        int_to_listnode(temp_node, temp_int)
        temp_node = reverse_list(temp_node.next)
        print_nodes(temp_node)
        return temp_node


if __name__ == '__main__':
    print(romanToInt("MDCCCLXXXIV"))
    print(romanToInt("M"))

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    a = Solution()
    a.addTwoNumbers(l1, l2)

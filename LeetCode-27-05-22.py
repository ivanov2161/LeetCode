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

    if temp.count('CM'):
        answer += temp.count('CM') * 900
        temp = temp.replace('CM', '')
    if temp.count('M'):
        answer += temp.count('M') * 1000
        temp = temp.replace('M', '')
    if temp.count('CD'):
        answer += temp.count('CD') * 400
        temp = temp.replace('CD', '')
    if temp.count('D'):
        answer += temp.count('D') * 500
        temp = temp.replace('D', '')
    if temp.count('XC'):
        answer += temp.count('XC') * 90
        temp = temp.replace('XC', '')
    if temp.count('C'):
        answer += temp.count('C') * 100
        temp = temp.replace('C', '')
    if temp.count('XL'):
        answer += temp.count('XL') * 40
        temp = temp.replace('XL', '')
    if temp.count('L'):
        answer += temp.count('L') * 50
        temp = temp.replace('L', '')
    if temp.count('IX'):
        answer += temp.count('IX') * 9
        temp = temp.replace('IX', '')
    if temp.count('X'):
        answer += temp.count('X') * 10
        temp = temp.replace('X', '')
    if temp.count('IV'):
        answer += temp.count('IV') * 4
        temp = temp.replace('IV', '')
    if temp.count('V'):
        answer += temp.count('V') * 5
        temp = temp.replace('V', '')
    if temp.count('I'):
        answer += temp.count('I') * 1
        temp = temp.replace('I', '')

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

        def reverse_list(head, tail=None):  # если это важно, то подглядел я только эту функцию =)
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

        def drop(node):
            n = node
            while n.next.next is not None:
                n = n.next
            n.next = None

        temp_int = node_to_int(reverse_list(l1)) + node_to_int(reverse_list(l2))
        temp_node = ListNode()
        int_to_listnode(temp_node, temp_int)
        temp_node = reverse_list(temp_node)
        drop(temp_node)
        print_nodes(temp_node)
        return temp_node


if __name__ == '__main__':
    print(romanToInt("MDCCCLXXXIV"))
    print(romanToInt("M"))

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    a = Solution()
    a.addTwoNumbers(l1, l2)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#     def __repr__(self):
#         return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
#
#
# def list_to_LL(arr):
#     if len(arr) < 1:
#         return None
#
#     if len(arr) == 1:
#         return ListNode(arr[0])
#     return ListNode(arr[0], next=list_to_LL(arr[1:]))
#
#
# def reverseList(head):
#     prev = None
#     while head:
#         next_node = head.next
#         head.next = prev
#         prev = head
#         head = next_node
#
#     return prev
#
#
# # test cases
# t1 = list_to_LL([1, 2, 3, 4, 5])  #ListNode(val=1, next={ListNode(val=2, next={ListNode(val=3, next={ListNode(val=4, next={ListNode(val=5, next={None})})})})})
# t2 = list_to_LL([1, 2])  #ListNode(val=1, next={ListNode(val=2, next={None})})
# t3 = list_to_LL([])
#
#
# # answers
# print(reverseList(t1))
# print(reverseList(t2))
# print(reverseList(t3))
#
#
# def add_two_numbers(l1, l2):
#     """
#     Difficult - Medium
#     You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
#     order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#     You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#     EXAMPLE: Input: l1 = [2,4,3], l2 = [5,6,4]
#                     Output: [7,0,8]
#                     Explanation: 342 + 465 = 807.
#     :param l1: Array
#     :param l2: Array
#     :return: Array of sum of reversed arrays
#     """
#
#     # Constraints
#
#     if len(l1) < 1 or len(l1) > 100 or len(l2) < 1 or len(l2) > 100:
#         print('Length of list should be in range(1, 100)')
#         return None
#
#     for i in l1:
#         if i < 0 or i > 9:
#             print('Numbers of list should be >= 0 and <= 9')
#             return None
#
#     for i in l2:
#         if i < 0 or i > 9:
#             print('Numbers of list should be >= 0 and <= 9')
#             return None
#
#     # Solution
#
#     answer = []
#
#     def reverse(array):
#         string = ''
#         for i in array[::-1]:
#             string += str(i)
#         return int(string)
#
#     numb_one = reverse(l1)
#     numb_two = reverse(l2)
#
#     for i in str(numb_one + numb_two):
#         answer.append(int(i))
#
#     return answer[::-1]
#
# n1 = 5335
# n2 = 0
#
# while n1 > 0:
#     # находим остаток - последнюю цифру
#     digit = n1 % 10
#     # делим нацело - удаляем последнюю цифру
#     n1 = n1 // 10
#     # увеличиваем разрядность второго числа
#     n2 = n2 * 10
#     # добавляем очередную цифру
#     n2 = n2 + digit
#
# print('"Обратное" ему число:', n2)

s = 'xbcabcbbxdfvdfbdfbqwertyuiop'

print(s[2:len(s)])

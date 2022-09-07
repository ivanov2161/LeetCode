from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

        temp_list = []
        temp_list_node = ListNode()

        def append(node, val):  # Функция для добавления элементов в ListNode
            while node.next:
                node = node.next
            node.next = ListNode(val)

        for i in lists:  # Добавление элементов list[[ListNode]] в список
            while i:
                temp_list.append(i.val)
                i = i.next

        for i in sorted(temp_list):  # Добавление в итоговый ListNode
            append(temp_list_node, i)

        return temp_list_node.next  # теперь до меня дошло как избавиться от первого "0" )))


A = ListNode(1, ListNode(4, ListNode(5)))
B = ListNode(1, ListNode(3, ListNode(4)))
C = ListNode(2, ListNode(6))

list_of_nodes = [A, B, C]

sorted_list_node = Solution().mergeKLists(list_of_nodes)

while sorted_list_node:
    print(sorted_list_node.val, end=' ')
    sorted_list_node = sorted_list_node.next

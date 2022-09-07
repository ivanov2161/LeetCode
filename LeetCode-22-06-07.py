from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Input: n = 19
        Output: true
        Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
        :param n:
        :return:
        '''

        if n == 1:
            return True
        elif n == 58:
            return False
        x = 0
        temp_numb = list(str(n))
        for i in temp_numb:
            x += int(i) * int(i)
        print(x)

        return Solution().isHappy(x)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        temp_list = []
        out_listnode = ListNode()

        def append(node, val):  # Функция для добавления элементов в ListNode
            while node.next:
                node = node.next
            node.next = ListNode(val)

        while list1:
            temp_list.append(list1.val)
            list1 = list1.next

        while list2:
            temp_list.append(list2.val)
            list2 = list2.next

        for i in sorted(temp_list):
            append(out_listnode, i)

        return out_listnode

    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        [1,1,2] with O(1)
        :param nums:
        :return:
        '''
        # Length of the update array
        count = 0
        # Loop for all the elements in the array
        for i in range(len(nums)):
            # If the current element is equal to the next element, we skip
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            # We will update the array in place
            nums[count] = nums[i]
            count += 1
        return count


print(Solution().isHappy(19))
print(Solution().removeDuplicates([1, 1, 2]))

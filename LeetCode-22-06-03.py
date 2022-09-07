class Solution(object):

    def letterCombinations(self, digits: str) -> list[str]:
        """
        :type digits: str
        :rtype: List[str]
        """

        letters_of_numb = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        temp_list = []

        for i in digits:
            temp_list.append(letters_of_numb[i])
        self.position = 0
        out_list = []

        def rec(array: list[str]) -> list[str]:
            if self.position < len(array):
                out_list.append(array[self.position][self.position])
                self.position += 1
                rec(array)
            else:
                position = 0
                return out_list

        rec(temp_list)
        return out_list

    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Example: Input: strs = ["flower","flow","flight"]
                Output: "fl"
        :type strs: List[str]
        :rtype: str
        """

        out_string = ""

        if strs is None or len(strs) == 0:
            return out_string

        for i in range(0, len(min(strs, key=len))):
            temp_string = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != temp_string:
                    return out_string
            out_string += temp_string

        print(out_string)
        return out_string

    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
        :type s: str
        :rtype: bool
        """
        char_list = ['(', ')', '{', '}', '[', ']']
        temp_string = s
        count_char = 0

        for i in char_list:
            if i in s:
                count_char += temp_string.count(i)
                temp_string = temp_string.replace(i, '')

        print(temp_string)
        print(count_char)

        if temp_string == '' and count_char % 2 == 0:
            print(True)
            return True
        else:
            print(False)
            return False

    def plusOne(self, digits: list[int]) -> list[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = ''

        for i in digits:
            temp += str(i)

        temp = int(temp) + 1
        *temp, = str(temp)
        return temp

    def singleNumber(self, nums: list[int]) -> int:
        '''

        :param nums:
        :return:
        '''
        res = nums[0]

        for i in nums[1: len(nums)]:
            res = res ^ i

        return res

a = Solution()

print(a.letterCombinations('239'))
print(a.singleNumber([4, 4, 2, 9, 1, 2, 1]))
a.longestCommonPrefix(["flower", "flower", "flower", "flower"])
a.isValid('{[]}')
a.plusOne([4, 3, 2, 1])

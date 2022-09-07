class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = list()
        for i, j in enumerate(nums):
            max_sum.append(j)
            j += sum(nums[i + 1:])
            max_sum.append(j)
        return max(max_sum)

    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(' ')
        a = list(filter(None, a))
        return len(a[-1])


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().lengthOfLastWord("luffy is still joyboy"))


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
        needle is not part of haystack.

        :param haystack: str
        :param needle: str
        :return: int
        '''

        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1



    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

    def climbStairs(self, n: int) -> int:
        return self.fib(n + 1)



first = 'hello'
second = 'll'


print(Solution().strStr(first, second))
print(Solution().climbStairs(4))







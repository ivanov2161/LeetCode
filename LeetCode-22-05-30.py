class Solution(object):
    def reverse(self, x):  # The first task
        """
        Difficult - Medium
        Given a signed 32-bit integer x, return x with its digits reversed.
        If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        :type x: int
        :rtype: int
        """
        def check(number):
            if number < -pow(2, 31) or number > pow(2, 31):
                return 0
            else:
                return number

        a = abs(x)
        a = int(str(a)[::-1])
        if x < 0:
            a *= -1
        return check(a)

    def setZeroes(self, matrix):  # The second task
        """
        Difficult - Medium
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        EXAMPLE: Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
                Output: [[1,0,1],[0,0,0],[1,0,1]]
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Solution

        def reverse(array):
            array_rev = []
            for i in range(len(array[0])):
                array_rev.append([])

            for i in array:
                for x, y in enumerate(i):
                    array_rev[x].append(y)
            return array_rev

        def setZero(array):
            for i, j in enumerate(array):
                if 0 in j:
                    for x, y in enumerate(j):
                        j[x] = 0

        def compile_array(array, array_two):
            array_rev = []
            for i in range(len(array)):
                array_rev.append([])

            for i, j in enumerate(array):
                for x, y in enumerate(j):
                    if array[i][x] == array_two[i][x]:
                        array_rev[i].append(y)
                    else:
                        array_rev[i].append(0)
            return array_rev

        b = reverse(matrix)
        setZero(matrix)
        setZero(b)
        c = reverse(b)
        d = compile_array(matrix, c)

        for i, j in enumerate(d):
            matrix[i] = j


# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[1, 1, 1, 0], [1, 2, 1, 1], [0, 1, 1, 1]]

a = Solution()
print(a.reverse(-1534236))
a.setZeroes(matrix)
print(matrix)

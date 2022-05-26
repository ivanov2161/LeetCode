def two_sum(nums, target):
    """
    Difficult - Easy
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add
    up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    EXAMPLE: Input: nums = [2,7,11,15], target = 9
            Output: [0,1]
            Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    :param nums: Array
    :param target: Numb
    :return: Array of two indices
    """

    # Constraints

    if len(nums) < 2 or len(nums) > 10e+4:
        print('Length of array should be >= 2 and <= 10^4')
        return None

    for i in nums:
        if i < -10e+9 or i > 10e+9:
            print('Numb of array should be >= -10^9 and <= 10^9')
            return None

    if target < -10e+9 or target > 10e+9:
        print('Target should be >= -10^9 and <= 10^9')
        return None

    # Solution

    for i in range(len(nums)):
        for j in range(len(nums)):
            j = i + j + 1
            if j >= len(nums):
                break
            if nums[i] + nums[j] == target:
                array = [i, j]
                print(array)
                return array

    print('No sum of number = target')


def palindrome_number(x):
    """
    Difficult - Easy
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    EXAMPLE: 121 is a palindrome while 123 is not.
    :param x: Any integer number
    :return: True or False
    """
    if x < -2e+31 or x > 2e+31 - 1:
        return None

    y = 0
    i = x

    while i > 0:
        digit = i % 10
        i = i // 10
        y = y * 10
        y = y + digit

    if x == y:
        return True
    else:
        return False


two_sum([2, 7, 11, 15], 9)

palindrome_number(121)

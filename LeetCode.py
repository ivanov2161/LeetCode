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

    # Constraints

    if x < -2e+31 or x > 2e+31 - 1:
        return None

    # Solution

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


def add_two_numbers(l1, l2):  # Здесь я лоханулся и сделал с массивами задачу, а надо было с ListNode - займусь позже =)
    """
    Difficult - Medium
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
    order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    EXAMPLE: Input: l1 = [2,4,3], l2 = [5,6,4]
                    Output: [7,0,8]
                    Explanation: 342 + 465 = 807.
    :param l1: Array
    :param l2: Array
    :return: Array of sum of reversed arrays
    """

    # Constraints

    if len(l1) < 1 or len(l1) > 100 or len(l2) < 1 or len(l2) > 100:
        print('Length of list should be in range(1, 100)')
        return None

    for i in l1:
        if i < 0 or i > 9:
            print('Numbers of list should be >= 0 and <= 9')
            return None

    for i in l2:
        if i < 0 or i > 9:
            print('Numbers of list should be >= 0 and <= 9')
            return None

    # Solution

    answer = []

    def reverse(array):
        string = ''
        for i in array[::-1]:
            string += str(i)
        return int(string)

    numb_one = reverse(l1)
    numb_two = reverse(l2)

    for i in str(numb_one + numb_two):
        answer.append(int(i))

    return answer[::-1]


def lengthOfLongestSubstring(s):
    """
    Difficult - Medium
    Given a string s, find the length of the longest substring without repeating characters.
    EXAMPLE: Input: s = "abcabcbb"
                    Output: 3
                    Explanation: The answer is "abc", with the length of 3.
    :param s:
    :return:
    """

    # Constraints 0 <= s.length <= 5 * 104

    if len(s) < 0 or len(s) > 5e+4:
        return None

    if len(s) == 0:
        return 0

    # Solution

    temp_array = [s[0]]
    max_length = []
    count = 0
    o = 0
    x = 0

    for y in s:
        for i in s[o:len(s)]:
            for j in temp_array:
                if i == j:
                    count += 1
            x += 1
            if count == 0 and not x - len(temp_array) > 1:
                temp_array.append(i)
            count = 0
        x = 0
        max_length.append(len(temp_array))
        o += 1
        try:
            temp_array = [s[o]]
        except:
            pass

    return max(max_length)


two_sum([2, 7, 11, 15], 9)
print(palindrome_number(121))
print(add_two_numbers([3, 4, 5], [2, 4, 5]))
print(lengthOfLongestSubstring("abcdefghiiiij,-./:;<=>?@[\\]^_`{|}~ abcde abc['"))

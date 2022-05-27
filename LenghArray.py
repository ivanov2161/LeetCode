def lengthOfLongestSubstring(s):


    def lengthOfLongestSubstring(s):
        start = 0
        maxlength = 0
        substring = {}  # Определить подстроку, здесь {} - словарь, может хранить любой объект

        for i, j in enumerate(s):
            if j <= substring[j]: # если в подстроке
                start = substring[j] + 1 # Окно сдвигается назад
            else:
                maxlength = max(maxlength, i - start + 1)
                substring[j] = i

        print(maxlength)
        return maxlength



print(lengthOfLongestSubstring('abcabcbb'))
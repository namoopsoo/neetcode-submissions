class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i = 0
        j = 1
        substring = longest = s[i:j]

        while True:
            if j == len(s):
                break
            # print("ok", j, len(s))
            new_char = s[j] 

            if new_char in set(substring):
                # update i, after that character, 
                index = substring.index(new_char)
                i = i + index + 1
            j += 1
            substring = s[i:j]
            if len(substring) > len(longest):
                longest = substring

        return len(longest)
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [
            x for x in s.lower()
            if x.isalnum()
        ]
        if len(s) in [0, 1]:
            return True

        # even length,
        # => e.g. len(s) = 4, and len(s)//2 = 2, 
        # so we compare [0, 1], with [3, 2]

        # odd length, 
        # => e.g. len(s) = 5, len(s)//2 = 2
        # so we compare [0, 1], with [4, 3], ignoring 2

        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return False

        return True

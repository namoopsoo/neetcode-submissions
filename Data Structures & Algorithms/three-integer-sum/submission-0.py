from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combos = set()
        for a, b, c in combinations((nums), 3):
            if a + b + c == 0:
                combos.add(
                    tuple(sorted([a,b,c]))
                )

        return [list(x) for x in combos]
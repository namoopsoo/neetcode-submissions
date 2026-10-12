from itertools import combinations
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # what if we have a hashmap for all the numbers, 
        # then , iterating just across two, , a O(1) look up for the third, 
        # this could be a O(n^2) method
        # but the indexes must be distinct 
        combos = set()
        hash = defaultdict(list)
        for i, x in enumerate(nums):
            hash[x].append(i)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                complement = -1 * (nums[i] + nums[j])

                # if the complement is there, it must have a distinct index
                if found := hash[complement]:
                    if set(found) - {i, j}:
                        combos.add(
                            tuple(sorted([
                                complement, nums[i], nums[j]
                            ]))
                        )
        return [list(x) for x in combos]

    def threeSum_combinations(self, nums: List[int]) -> List[List[int]]:
        # O(n^3)
        combos = set()
        for a, b, c in combinations((nums), 3):
            if a + b + c == 0:
                combos.add(
                    tuple(sorted([a,b,c]))
                )

        return [list(x) for x in combos]
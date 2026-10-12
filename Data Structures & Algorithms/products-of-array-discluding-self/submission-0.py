from operator import mul
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = []
        for i, x in enumerate(nums):
            if x == 0:
                zeroes.append(i)
                if len(zeroes) > 1:
                    return [0]*len(nums)
            else:
                product *= x

        # one zero, then all outputs are zeroes, except index with 0.
        if zeroes:
            zero_index = zeroes[0]
            return [
                0 if i != zero_index else product
                for i in range(len(nums))
            ]

        # no zeroes
        return [
            int(product/x) for x in nums
        ]



def idea1(nums):
    product = reduce(
        mul, nums
    )
    return [
        (int(product/x) if x != 0 else product) 
        for x in nums

    ]
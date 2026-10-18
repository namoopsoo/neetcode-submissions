from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # find the largest pile, that will be the max
        max_pile = max(piles)
        vec = (range(1, max_pile + 1))

        best_k = None
        best_k = bs(piles, vec, h, best_k)
        return best_k
        ...


def bs(piles, vec, h, best_k):
    # check if middle is under h
    length = len(vec)

    if length == 0:
        return best_k
    middle_i = int(length/2)
    #if middle_i == 0:
    #    return False

    hours = check(vec[middle_i], piles)

    # works? nice, ok lets slow it down,
    if hours <= h:
        best_k = vec[middle_i]
        return bs(piles, vec[:middle_i], h, best_k)

    # no, k is too small, speed it up, 
    if hours > h:
        # too many, need to increase k
        result = bs(piles, vec[middle_i + 1:], h, best_k)
        return result
        #if result is False:
        #    return bs(piles, vec[:middle_i], h)



def check(k, piles):
    """calculate how many hours it takes to munch through the piles given a rate of k
    """
    hours = 0
    for num_bananas in piles:
        hours += ceil(num_bananas/k)

    return hours


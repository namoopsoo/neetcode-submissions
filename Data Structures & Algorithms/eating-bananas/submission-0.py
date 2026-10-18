from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # find the largest pile, that will be the max
        max_pile = max(piles)
        vec = list(range(1, max_pile + 1))
        best_k = bs(piles, vec, h)

        ...

        # then walk backwards one number at a time
        while True:
            k = best_k - 1
            if k == 0:
                return best_k
            hours = check(k, piles)
            if hours > h:
                # went over, so we can return best_k
                return best_k
            
            best_k = k

def bs(piles, vec, h):
    # check if middle is under h
    length = len(vec)
    middle_i = int(length/2)
    #if middle_i == 0:
    #    return False

    hours = check(vec[middle_i], piles)

    # works? nice return it
    if hours <= h:
        return vec[middle_i]

    if hours > h:
        # too many, need to increase k
        result = bs(piles, vec[middle_i + 1:], h)
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


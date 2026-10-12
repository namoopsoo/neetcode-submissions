import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # if we update L, save the best (L,H) so far
        # if L is not set, dont set H

        # set first as Low
        low_i = 0
        low = prices[0]
        high_i = None 
        high = 0
        best_low_high_indices = None
        best_low_high = 0

        for i in range(1, len(prices)):
            p = prices[i]
            
            # if p is lower, update L
            if p < low:
                # update best jump if high defined
                if high_i:
                    best_low_high_indices = low_i, high_i
                    best_low_high = high - low
                    high_i = None
                    high = 0

                # update low 
                low_i = i
                low = p
            elif low < p and high < p:
                high = p
                high_i = i
                if best_low_high < (high - low):
                    best_low_high = high - low
                    
        return best_low_high

            





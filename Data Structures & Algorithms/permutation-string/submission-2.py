from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # find frequency of s1 
        d1 = dict(Counter(s1))

        WINDOW_SIZE = len(s1)

        # starting s2 frequency
        d2 = initialize_default_dict(s2[0:WINDOW_SIZE])

        # slide the window
        for i in range(len(s2) - WINDOW_SIZE + 1):
            if d1 == d2:
                return True
            
            # otherwise, update d2
            j = i + WINDOW_SIZE  # j points to one position after window
            if j == len(s2):
                break

            # remove s2[i]
            first = s2[i]
            d2[first] -= 1
            if d2[first] == 0:
                del d2[first]

            # add next  
            d2[s2[j]] += 1

        return False

def initialize_default_dict(s):

    d = defaultdict(int)
    for k, v in dict(Counter(s)).items():
        d[k] = v
    return d


        
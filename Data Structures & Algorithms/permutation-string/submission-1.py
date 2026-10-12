from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ...

        # find frequency of s1 
        d1 = dict(Counter(s1))

        SIZE = len(s1)

        # starting s2 frequency
        w = s2[0:SIZE]
        d2 = initialize_default_dict(s2[0:SIZE])

        # slide 
        for i in range(len(s2) - len(s1) + 1):
            if d1 == d2:
                return True
            
            # otherwise, update d2
            # j points to one position after window
            j = i + SIZE

            # remove s2[i]
            first = s2[i]
            d2[first] -= 1  # delete?
            if d2[first] == 0:
                del d2[first]


            if j == len(s2):
                break
            # add next  
            d2[s2[j]] += 1

        return False

def initialize_default_dict(s):

    d = defaultdict(int)
    for k, v in dict(Counter(s)).items():
        d[k] = v
    return d


        
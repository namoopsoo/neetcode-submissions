import bisect

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ...
        deq = DEQ()
        [deq.insert2(x) for x in nums]
        longest_seq, longest = find_longest(deq.sorted_list)
        return longest 


class DEQ:
    def __init__(self):
        self.forward = {}
        self.seen = set()
        self.min = float("+inf")

        self.sorted_list = []

    def insert(self, elem):
        if elem < self.min:
            self.min = elem

        self.seen.add(elem)

        before = elem - 1 

        if before in self.forward:
            self.forward[before] = elem

        after = elem + 1
        if after in self.seen:
            self.forward[elem] = after     
        else:
            self.forward[elem] = None   
    def insert2(self, elem):
        if elem in self.seen:
            return
        bisect.insort(self.sorted_list, elem)
        self.seen.add(elem)


def find_longest(sorted_list):
    longest = 1
    longest_seq = []
    prev = sorted_list[0]
    seq = [prev]
    for i in range(1, len(sorted_list)):
        elem = sorted_list[i]
        if prev + 1 == elem:
            seq.append(elem)
            if len(seq) > longest:
                longest_seq = seq
                longest = len(seq)
        else:
            seq = [elem]
        prev = elem
    return longest_seq, longest


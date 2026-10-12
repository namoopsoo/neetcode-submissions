from typing import List
from copy import deepcopy

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vec = Vec(matrix)
        if vec.length() == 1:
            return vec.at_index(0) == target
        return bs(vec, target)

class Vec:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = m = len(matrix)
        self.n = n = len(matrix[0])

        self.i = 0
        self.j = m*n
    
    def at_index(self, x):
        i, j = map_func(x, self.m, self.n)
        return self.matrix[i][j]

    def slice(self, start, end):
        foo = deepcopy(self)
        foo.i = start
        foo.j = end
        return foo

    def length(self):
        return self.j - self.i


def bs(vec, target):
    length = vec.length()
    middle_index = vec.i + int(length/2)

    # middle?
    middle = vec.at_index(middle_index)
    print(f"bs, {vec.i=}, {middle_index=}, {vec.j=}, ...({middle=})")

    if target == middle:
        return True

    # look at first half
    if target < middle and vec.i < middle_index:
        foo = vec.slice(vec.i, middle_index)
        left_result = bs(foo, target)
        if left_result:
            return True

    # look at second half
    if middle_index + 1 < vec.j:
        foo = vec.slice(middle_index + 1, vec.j)
        right_result = bs(foo, target)
        if right_result:
            return True

    return False

def map_func(x, m, n):
    j = x % n
    i = x // n
    return int(i), int(j)

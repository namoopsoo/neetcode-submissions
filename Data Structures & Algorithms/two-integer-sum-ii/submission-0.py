class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                x = numbers[i]
                y = numbers[j]
                if x + y == target:
                    return [i + 1, j + 1]
                
                if x + y > target:
                    # should stop early but thats tricky
                    ...
                
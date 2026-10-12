class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        self.numbers = numbers
        self.target = target
        return self.j_binary_search()

    def j_binary_search(self):    
        # iterate i, one at a time, but j use binary search
        last = len(self.numbers) - 1
        print("last", last)

        for i in range(len(self.numbers)):
            result = self.bs(i, i+1, last)
            if isinstance(result, list):
                return result

    @staticmethod    
    def get_middle(a, b):
        if a + 1 == b:
            return b
        if a == b:
            return b

        return a + (b - a)//2

    def bs(self, i, first, last):
        if first > last:
            return "nope"

        j = self.get_middle(first, last)
        print(f"middle {first}, {last} ==> {j}")
        x = self.numbers[i]
        y = self.numbers[j]

        # return if N[i] + N[j] give target
        if x + y == self.target:
            return [i + 1, j + 1]
        
        # too small? , search bigger
        if x + y < self.target:
            return self.bs(i, j+1, last)

        # too big? , search smaller 
        return self.bs(i, first, j-1)

    @staticmethod
    def brute(numbers, target):    
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                x = numbers[i]
                y = numbers[j]
                if x + y == target:
                    return [i + 1, j + 1]
                
                if x + y > target:
                    # should stop early but thats tricky
                    ...
                
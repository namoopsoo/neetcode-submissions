class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # ok, each list of digits is ambiguous because each digit can correspond to three letters, for 2, 3 etc and four letters for 7 and 9. 
        # So for each sequence of digits, lets go through and list off unambiguously, every possible sequence of letters.
        # the number of possible letter sequences is equal to (3^n)x(4^m) for the n 3-letter numbers and m 4-letter numbers. So that's a lot !
        # 
        # Algorithms, you can use DFS or BFS
        # Let's do DFS  idea first;  use recursion, recursively DFS's through the tree of possibilities. You can solve it with 
        ...
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi", 
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        return dfs("", digits, mappings)

def dfs(str_sequence, digits, mappings) -> List[str]:
    """
    Parameters
    ----------
    str_sequence: the string sequence so far
    digits: the remaining unprocessed digits
    """
    # Are we at the end
    if not digits:
        return [str_sequence]

    # pick off next digit a follow the possible paths
    digit = digits[0]
    seqs = []
    for letter in mappings[digit]:
        vec = dfs(
            str_sequence + letter,
            digits[1:],
            mappings,
        )
        seqs.extend(vec)

    return seqs


        
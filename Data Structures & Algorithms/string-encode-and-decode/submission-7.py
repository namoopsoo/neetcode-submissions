import re

PAD = "9283746598"

class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "special_edge_case_0"
        if len(strs) == 1:
            return "special_edge_case_1=" + strs[0]

        return PAD.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "special_edge_case_0":
            return []
        if s.startswith("special_edge_case_1"):
            return [s[len("special_edge_case_1="):]]

        start = 0 
        words = []
        m = None
        for i, m in enumerate(re.finditer(PAD, s)):
            end = m.start()
            word = s[start:end]
            words.append(word)
            start = m.end()
        if m:
            print("s is", s)
            words.append(s[m.end():])
        else:
            return [""]
        return words


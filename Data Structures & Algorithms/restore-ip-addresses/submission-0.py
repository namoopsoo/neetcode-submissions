import re

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Must insert three dots. Find all the valid locations for them.
        # Maybe start from the left most positions for three nested for loops , iterate all possible and use a regex to check if legal. 

        valid_ip = r"([1-9]([0-9])))\."
        length = len(s)
        potentials = []
        valids = []
        # "www.xxx.yyy.zzz"
        #  0.............^L-1

        for i in range(1, (length - 2)):
            for j in range(i+1, length - 1):
                for k in range(j+1, length):
                    w, x, y, z = s[:i], s[i:j], s[j:k], s[k:]
                    ip = w + "." + x + "." + y + "." + z
                    potentials.append(ip)
                    for octet in [w, x, y, z]:
                        if (
                            (int(octet) == 0 and octet != "0")
                            or (octet.startswith("0") and int(octet) != 0)
                            or not (0 <= int(octet) <= 255)
                        ):
                            print("❌"+ ip)
                            break
                    else:
                        valids.append(ip)
                        print("✅"+ ip)
        return valids



        
        
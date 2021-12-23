class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}
        for i, data in enumerate(s):
            # print(a)
            if a.get(data):
                a[data] = 99999
            else:
                a[data] = i+1
        # print(a)
        if min(a.values()) > 90000:
            return -1
        else:
            return min(a.values())-1
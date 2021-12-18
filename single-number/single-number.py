class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if a.get(i):
                del a[i]
            else:
                a[i] = 1
        return list(a.keys())[0]
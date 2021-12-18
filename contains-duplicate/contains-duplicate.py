class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = {}
        
        for i in nums:
            if a.get(i):
                return True
            else:
                a[i] = 1
        return False
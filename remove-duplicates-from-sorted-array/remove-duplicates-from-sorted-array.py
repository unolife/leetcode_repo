class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        appear = []
        for idx, data in enumerate(nums):
            if idx == 0:
                continue
            else:
                if data == nums[idx-1]:
                    ans += 1
                    appear.append(data)
                    
        for i in appear:
            nums.remove(i)
            

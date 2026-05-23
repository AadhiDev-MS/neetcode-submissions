class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        j=0
        nums.sort()
        for i in range(len(nums)):

            if nums[i]!=j:
                return j
            else:
                j=j+1
        return j
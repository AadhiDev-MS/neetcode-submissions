class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dick={}
        for num in nums:
            if num in dick:
                return True
            else:
                dick[num]=1

        return False



        
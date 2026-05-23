class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if (digits[-1-i])!=9:
                digits[-1-i]+=1
                break
            else:
                digits[-1-i]=0
        if digits[0]==0:
            digits.insert(0,1)          


        return digits        
        
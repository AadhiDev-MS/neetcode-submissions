class Solution:
    def isHappy(self, n: int) -> bool:
        number=str(n)
        previous=set()
        while 1 not in previous:
            sum=0
            for i in range(len(number)):
                sum+=int(number[i])**2
            number=str(sum)
            if sum in previous:
                return False
            else:
                previous.add(sum)    
        return True        




        
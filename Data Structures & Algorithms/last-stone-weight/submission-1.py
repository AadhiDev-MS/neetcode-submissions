class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        length = len(stones)

        for i in range(length):

            if length == 1:
                return stones[0]

            if len(stones) == 0:
                return 0    

            else:
                if stones[-1] == stones[-2]:
                    del stones[-2]
                    del stones[-1]
                    
                    length -= 2

                elif stones[-1] > stones[-2]:
                    stones[-1] = stones[-1] - stones[-2]
                    del stones[-2]
                    length -= 1
                    stones.sort()

       

        return stones[0]




        
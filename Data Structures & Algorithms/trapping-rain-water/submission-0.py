from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        """
         we need to compute the area and basically whenver this is zero, 
         we see a gap, we need to compute that area between bars 
            * that 0 can't be first and last indices
        

        they were asking for maximum ---> use of stack 






         """

        l = 0
        r = len(height) - 1
        leftmax = height[l]
        rightmax = height[r]
        area = 0

        while l < r:
            if height[l] < height[r]:
                leftmax = max(leftmax, height[l])
                area+=leftmax - height[l]
                l+=1
            else:
                rightmax = max(rightmax, height[r])
                area+=rightmax - height[r]
                r-=1

        return area

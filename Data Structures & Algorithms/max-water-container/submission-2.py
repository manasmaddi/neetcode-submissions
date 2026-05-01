class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxium amount of water a conatiner can store 

        l, r = 0, len(heights)-1
        maximum_area = 0

        while l<=r:
            if heights[l] >= heights[r]:
                area = heights[r] * (r-l)  
            else:
                area = heights[l] * (r-l)

            maximum_area = max(maximum_area,area)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return maximum_area
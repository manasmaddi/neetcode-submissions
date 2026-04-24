class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need to find the area enclosed 

        # we need some benchmarking here of how to obtain this 
        """
        so what is breaking here ?
        1. let's take a indice and start cosntructing 
        2. so we start a number right , and then we add on no matter what even if it slow, but if the value 
        is more than the starting value it is a break, region covered is over.
        3. and then area is calculated by by starting indices and then the breaking indices 
        4. we maintin a area and called max_area and return max_area . 


        the problem is this will take a significant time to compute, we need something 
        to do smart here...

        we can't have two pointers front and back, we don't know what's there in middle so no use with that 






        """
        i = 0
        j = len(heights)-1
        area = 0

        while i<j:
            min_height = min(heights[i],heights[j])
            current_area = (j-i) * min_height
            if current_area > area:
                area = current_area
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return area
            
            

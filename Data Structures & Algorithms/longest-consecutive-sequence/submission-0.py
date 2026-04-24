class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # we use set to avoid duplicates 

        remove_duplicates = (set(nums))
        max_res = 0
       
        for i in remove_duplicates:
            current = i
            present_count = 0

            while current in remove_duplicates:
                present_count += 1
                current+=1
            max_res = max(max_res,present_count)
        return max_res



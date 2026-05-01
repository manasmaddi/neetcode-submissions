class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minimal --> sliding window 

        # whose sum is greater than target 

        l = 0
        minimal_length = len(nums)+1


        current_sum = 0

        for r in range(len(nums)):
            current_sum = current_sum + nums[r] # we add sums 

            while current_sum >= target: # this is the breaking condition 
                # we just remove teh sliding pointer 
                minimal_length = min(minimal_length,r-l+1)
                current_sum = current_sum - nums[l]
                l+=1
        return minimal_length if minimal_length <= len(nums) else 0
                



            
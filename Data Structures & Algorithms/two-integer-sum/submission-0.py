class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sad = {}
        for i,num in enumerate(nums):
            required = target-num
            if required in sad:
                return [sad[required], i]
            sad[num]=i
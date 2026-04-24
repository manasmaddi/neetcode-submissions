class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set()
        for i in nums:
            if i in no_duplicates:
                return True
            no_duplicates.add(i)
        return False
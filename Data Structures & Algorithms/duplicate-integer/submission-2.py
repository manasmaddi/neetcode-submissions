class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set()
        for i in nums:
            if i not in no_duplicates:
                no_duplicates.add(i)
            else:
                return True
        return False
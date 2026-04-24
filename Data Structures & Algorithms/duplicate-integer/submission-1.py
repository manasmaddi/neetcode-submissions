class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1

        for j in store.values():
            if j > 1:
                return True
        return False
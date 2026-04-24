class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # find all elements that appear more than n/3 toimes 
        n = len(nums)
        a = {}
        b = []
        c = []
        minimum_threshold = n//3
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i] = 1
            if a[i] > minimum_threshold:
                b.append(i)
        for j in b:
            if j not in c:
                c.append(j)
        return c
            
        
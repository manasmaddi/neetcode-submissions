class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # returning the indices, and no using the same element twice, 
        # meaning once the element is done, no using it 

        # only one valid solution 

        # it is already sorted, any clues with that ?????


      #  given_numbers = set(numbers) # just to avoid any duplicates 
        
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
            


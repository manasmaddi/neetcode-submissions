class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        # choosing x 

        # replace with english capital letters ??
        # they give k number , you can choose any other english letters and replace that with the substring and return it 

        # for example

        AAABABB - >> k = 1 , so choose how are you gonna choose 



        """

        count = {}
        result = 0 
        l , maximum_frequency = 0,0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1 # hashmap built 
            maximum_frequency = max(maximum_frequency,count[s[r]])

            while (r-l+1) - maximum_frequency > k:
                count[s[l]] -=1
                l+=1
            result = max(result, r-l+1)
        return result


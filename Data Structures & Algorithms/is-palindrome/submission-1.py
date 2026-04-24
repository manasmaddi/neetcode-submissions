import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # what if there is no alnum function used
        pattern = r'[a-zA-Z0-9]'
        filtered_s = ""
        for i in s:
            if re.match(pattern,i):
                filtered_s += i.lower()

        reversed_s = ""
        for j in filtered_s:
            reversed_s = j + reversed_s
      
        if(filtered_s == reversed_s):
            return True
        else:
            return False

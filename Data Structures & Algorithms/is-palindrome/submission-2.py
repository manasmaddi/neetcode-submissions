class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s:
            if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >=65 and ord(i) <=90) or (ord(i) >= 97 and ord(i) < 122):
                a.append(i.lower())
        print(a)

        i = 0
        j = len(a) - 1
        while i <j:
            if a[i] != a[j]:
                return False
            i = i+1
            j= j-1
        return True



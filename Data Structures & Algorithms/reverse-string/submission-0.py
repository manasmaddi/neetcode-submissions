class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = len(s)
        for i in range(a // 2):
            s[i], s[a-1-i] = s[a-1-i], s[i]
        return s
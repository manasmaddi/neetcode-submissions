class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary to keep a count of all the unique characters in t.
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # Left and Right pointer
        l, r = 0, 0

        
        formed = 0
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                # Move the left pointer ahead.
                l += 1    

            # Keep moving the right pointer to find a new window
            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
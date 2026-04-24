class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            current_char = s[end]
            
            if current_char in char_map:
                start = max(start, char_map[current_char] + 1)
            char_map[current_char] = end
            
            max_length = max(max_length, end - start + 1)
            
        return max_length
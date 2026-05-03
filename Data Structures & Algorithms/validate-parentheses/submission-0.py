class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        lookup = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in lookup:
                # If stack is empty or top doesn't match, it's invalid
                if not stack or stack.pop() != lookup[char]:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # A valid string must result in an empty stack
        return not stack
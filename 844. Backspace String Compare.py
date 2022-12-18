# https://leetcode.com/problems/backspace-string-compare/
# time complexity : O(n)
# space complexity : O(n)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for ch in s :
            if not stack_s and ch == '#':
                continue
            elif not stack_s or ch != '#':
                stack_s.append(ch)
            else:
                stack_s.pop()
            
        for ch in t :
            if not stack_t and ch == '#':
                continue
            elif not stack_t or ch != '#':
                stack_t.append(ch)
            else:
                stack_t.pop()
        
        if stack_s == stack_t:
            return True
        return False
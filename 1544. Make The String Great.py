# https://leetcode.com/problems/make-the-string-great/description/
# time complexity : O(n)
# space complexity : O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif ch.isupper() is True and ch.lower() == stack[-1]:
                    stack.pop()
            elif ch.islower() is True and ch.upper() == stack[-1]:
                    stack.pop()
            else :
                stack.append(ch)

        return ''.join(stack)
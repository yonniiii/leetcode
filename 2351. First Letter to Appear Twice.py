# https://leetcode.com/problems/first-letter-to-appear-twice/description/
# time complexity : O(n)
# space complexity : O(n)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = set()
        for i in range(len(s)):
            if s[i] in dic:
                return s[i]
            else :
                dic.add(s[i])
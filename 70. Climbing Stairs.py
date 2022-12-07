# https://leetcode.com/problems/climbing-stairs/description/
# time complexity : O(n)
# space complextiy : O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0,1,2]

        if n in [0,1,2]:
            return result[n]
        
        for i in range(3,n+1):
            result.append(result[i-1]+result[i-2])

        return result[n]

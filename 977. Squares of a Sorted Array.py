# https://leetcode.com/problems/squares-of-a-sorted-array/
# time complexity : O(nlogn)
# space complexity : O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range (len(nums)):
            result.append(nums[i]**2)
        
        result.sort()
        return result

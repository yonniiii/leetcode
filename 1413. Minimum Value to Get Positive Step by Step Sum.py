# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/
# time complexity : O(n)
# space complexity : O(n)

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        
        min_prefix_sum = min(prefix_sum)

        if min_prefix_sum > 0 :
            return 1
        else :
            return abs(min_prefix_sum) +1
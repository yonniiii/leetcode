# https://leetcode.com/problems/maximum-average-subarray-i/description/
# time complexity : O(n)
# space complexity : O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = max_sum =sum(nums[0:k])
        
        for i in range(1,len(nums)-k+1):
            sum_k = sum_k - nums[i-1] + nums[i+k-1]
            max_sum =  max(max_sum, sum_k)

        return max_sum/k
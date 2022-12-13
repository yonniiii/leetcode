# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# time complexity : O(n*m)
# space complexity : O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left +=1
            result = max (result,right-left+1)
        
        return result
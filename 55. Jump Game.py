class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_index = len(nums)-1
        for i in range(target_index-1,-1,-1):
            if i + nums[i] >= target_index:
                target_index = i 
        
        if target_index == 0 :
            return True
        else :
            return False